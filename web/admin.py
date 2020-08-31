from django.contrib import admin
from .models import Buy,Sell,Property,Stock,StockError,Deposit,Withdraw,Balance
# from . import models

@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display=[]
    for i in Buy._meta.fields:
        if i.name!= 'id':list_display.append(i.name)
    list_display=tuple(list_display)


@admin.register(Sell)
class SellAdmin(admin.ModelAdmin):
    list_display=[]
    for i in Sell._meta.fields:
        if i.name!= 'id':list_display.append(i.name)
    list_display=tuple(list_display)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display=[]
    for i in Property._meta.fields:
        if i.name!= 'id':list_display.append(i.name)
    list_display=tuple(list_display)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display=[]
    for i in Stock._meta.fields:
        if i.name!= 'id':list_display.append(i.name)
    list_display=tuple(list_display)


@admin.register(StockError)
class StockErrorAdmin(admin.ModelAdmin):
    list_display=[]
    for i in StockError._meta.fields:
        if i.name!= 'id':list_display.append(i.name)
    list_display=tuple(list_display)


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display=[]
    for i in Deposit._meta.fields:
        if i.name!= 'id':list_display.append(i.name)
    list_display=tuple(list_display)

@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display=[]
    for i in Withdraw._meta.fields:
        if i.name!= 'id':list_display.append(i.name)
    list_display=tuple(list_display)

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display=[]
    for i in Balance._meta.fields:
        if i.name!= 'id':list_display.append(i.name)
    list_display=tuple(list_display)
# admin.site.register(Buy)
# admin.site.register(Sell)
# admin.site.register(Property)
# admin.site.register(Stock)
# admin.site.register(StockError)
# admin.site.register(Deposit)

