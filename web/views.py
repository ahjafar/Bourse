from django.shortcuts import render
from .forms import AddBuyForm,AddSellForm,AddDepositForm,AddWithdrawForm
from django.contrib.auth.decorators import login_required
from .models import Buy,Property,Stock,Sell,Deposit,Withdraw,Balance
from .utils import check_stock,check_property,get_price
from math import ceil
import jdatetime
# from django.views.decorators.csrf import csrf_exempt

@login_required
def add_buy(request):
    if 'name' in request.POST:
        name=request.POST['name']
        if check_stock(name):
            user=request.user
            stock=Stock.objects.get(name=name)
            price=int(request.POST['price'])
            quantity=int(request.POST['quantity'])
            year=request.POST['year']
            month=request.POST['month']
            day=request.POST['day']
            Buy.objects.create(user=user,stock=stock,price=price,quantity=quantity,year=year,day=day,month=month)
            if Property.objects.filter(stock=stock,user=user).exists():
                p=Property.objects.get(stock=stock)
                p.price=(p.price*p.quantity+price*quantity)/(p.quantity+quantity)
                p.quantity=p.quantity+quantity
                p.save()
            else:
                Property.objects.create(user=user,stock=stock,price=price,quantity=quantity)
            context={}
            context['form']=AddBuyForm()
            context['message']='خرید اضافه شد.'
            return render(request,'Buy.html',context)
        else:
            context={}
            context['form']=AddBuyForm()
            context['ndisplay']="block"
            return render(request,'buy.html',context)
    else:
        context={}
        context['form']=AddBuyForm()
        return render(request,'buy.html',context)


@login_required
def add_sell(request):
    if 'name' in request.POST:
        name=request.POST['name']
        quantity=int(request.POST['quantity'])
        user=request.user
        stock=Stock.objects.get(name=name)
        if check_property(stock,quantity,user)==0:
            price=int(request.POST['price'])
            year=request.POST['year']
            month=request.POST['month']
            day=request.POST['day']
            Sell.objects.create(user=user,stock=stock,price=price,quantity=quantity,year=year,day=day,month=month)
            p=Property.objects.get(stock=stock)
            p.quantity=p.quantity-quantity
            p.save()
            if p.quantity==0:
                p.delete()
            context={}
            context['form']=AddBuyForm()
            context['message']='فروش اضافه شد.'
            return render(request,'sell.html',context)
        elif check_property(stock,quantity,user)==1:
            context={}
            context['form']=AddSellForm()
            context['ndisplay']="block"
            return render(request,'sell.html',context)
        else:
            context={}
            context['form']=AddSellForm()
            context['qdisplay']="block"
            return render(request,'sell.html',context)
    else:
        context={}
        context['form']=AddSellForm()
        return render(request,'sell.html',context)
    
    
@login_required
def property_table(request,n):
    prices,gains,values,gain_amounts=[],[],[],[]
    context={}
    p=Property.objects.filter(user=request.user)
    if n=='':n=1
    n=int(n)
    for i in p:
        price=get_price(i.stock.url)
        prices.append(price)
        values.append(price*i.quantity)
        gains.append("{:.2f}".format((price-i.price)/i.price*100))
        gain_amounts.append((price-i.price)*i.quantity)
    context['property']=sum(values)
    context['number']=len(p)
    context['gain']=sum(gain_amounts)
    context['range']=range(1,ceil(p.count()/10)+1)
    context['x']=zip(p[10*(n-1):10*n],range(10*(n-1)+1,10*n+1),prices[10*(n-1):10*n],gains[10*(n-1):10*n],values[10*(n-1):10*n],gain_amounts[10*(n-1):10*n])
    context['activation']={n:'activated'}
    return render(request,'property.html',context)


@login_required
def add_deposit(request):
    if 'amount' in request.POST:
        amount=request.POST['amount']
        year=request.POST['year']
        month=request.POST['month']
        day=request.POST['day']
        user=request.user
        Deposit.objects.create(user=user,amount=amount,year=year,month=month,day=day)
        if Balance.objects.filter(user=user).exists():
            b=Balance.objects.get(user=user)
            b.amount+=amount
            b.save()
        else:
            Balance.objects.create(user=user,amount=amount)
        context={}
        context['form']=AddDepositForm()
        context['message']='واریز وجه اضافه شد.'
        return render(request,'deposit.html',context)
    else:
        form=AddDepositForm()
        return render(request,'deposit.html',{'form':form})

@login_required
def add_withdraw(request):
    if 'amount' in request.POST:
        amount=int(request.POST['amount'])
        year=request.POST['year']
        month=request.POST['month']
        day=request.POST['day']
        user=request.user
        Withdraw.objects.create(user=user,amount=amount,year=year,month=month,day=day)
        context={}
        context['form']=AddWithdrawForm()
        if Balance.objects.filter(user=user).exists():
            b=Balance.objects.get(user=user)
            if b.amount>=amount:
                b.amount-=amount
                b.save()
                context['message']='برداشت وجه اضافه شد.'
            else:
                context['adisplay']='block'
        else:
            context['adisplay']='block'
        return render(request,'withdraw.html',context)
    else:
        form=AddWithdrawForm()
        return render(request,'withdraw.html',{'form':form})

@login_required
def deposit_table(request,n):
    context={}
    month=[]
    d=Deposit.objects.filter(user=request.user)
    if n=='':n=1
    n=int(n)
    context['range']=range(1,ceil(d.count()/10)+1)
    context['activation']={n:'activated'}
    for i in d[10*(n-1):10*n]:
        month.append(jdatetime.date.j_months_short_en.index(i.month)+1)
    context['x']=zip(d[10*(n-1):10*n],month)
    return render(request,'deposit-stats.html',context)

@login_required
def deposit_table(request,n):
    context={}
    month=[]
    w=Withdraw.objects.filter(user=request.user)
    if n=='':n=1
    n=int(n)
    context['range']=range(1,ceil(w.count()/10)+1)
    context['activation']={n:'activated'}
    for i in w[10*(n-1):10*n]:
        month.append(jdatetime.date.j_months_short_en.index(i.month)+1)
    context['x']=zip(w[10*(n-1):10*n],month)
    return render(request,'deposit-stats.html',context)