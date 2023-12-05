from django.contrib import admin
from .models import Client, Bill, Product, BillProduct

admin.site.register(Client)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(BillProduct)
