from django.shortcuts import render
from .forms import AddBuyForm,AddSellForm,AddDepositForm
from django.contrib.auth.decorators import login_required
from .models import Buy,Property,Stock,Sell,Deposit
from .utils import check_stock,check_property,get_price
from math import ceil
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
    prices,gains=[],[]
    context={}
    p=Property.objects.filter(user=request.user)
    if n=='':n=1
    n=int(n)
    for i in p[10*(n-1):10*n]:
        price=get_price(i.stock.url)
        prices.append(price)
        gains.append("{:.2f}".format((price-i.price)/i.price*100))
    context['range']=range(1,ceil(p.count()/10)+1)
    context['x']=zip(p[10*(n-1):10*n],range(10*(n-1)+1,10*n+1),prices,gains)
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
        context={}
        context['form']=AddDepositForm()
        context['message']='واریز وجه اضافه شد.'
        return render(request,'deposit.html',context)
    else:
        form=AddDepositForm()
        return render(request,'deposit.html',{'form':form})


@login_required
def deposit_table(request,n):
    context={}
    p=Deposit.objects.filter(user=request.user)
    if n=='':n=1
    n=int(n)
    context['property']=p[10*(n-1):10*n]
    context['range']=range(1,ceil(p.count()/10)+1)
    context['activation']={n:'activated'}
    return render(request,'deposit-stats.html',context)