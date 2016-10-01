from django.contrib import admin
from manager.models import Product, Sale

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'productName', 'created_at')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'created_at', 'updated_at')

admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
