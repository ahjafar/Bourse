from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def add_buy(request):
    return render(request,'buy.html')

@csrf_exempt 
def add_sell(request):
    #print(request.POST)
    c=request.POST.copy()
    return c
    