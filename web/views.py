from django.shortcuts import render
from .forms import AddBuyForm,AddSellForm
from django.contrib.auth.decorators import login_required
from .models import Buy,Property,Stock,Sell
from .utils import check_stock,check_property
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
            return render(request,'index.html')
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
            return render(request,'index.html')
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
    