from django.contrib import admin
from .models import Product, Category, Stock, Sale

class ProductAdmin(admin.ModelAdmin):
    list_display = ('item','unit_price', 'date_added', )
    list_display_links = ('item','unit_price','date_added')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    list_display_links = ('name', 'date_added')

class StockAdmin(admin.ModelAdmin):
    list_display = ('item','quatity', 'date_added', )
    list_display_links = ('item','quatity','date_added')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('item','cost','buyer', 'date_added', )
    list_display_links = ('item','cost', 'buyer', 'date_added')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.site_header = 'Administration Villa Ideal'