from django.contrib import admin
from .models import Buy,Sell,Property,Stock,StockError


admin.site.register(Buy)
admin.site.register(Sell)
admin.site.register(Property)
admin.site.register(Stock)
admin.site.register(StockError)
