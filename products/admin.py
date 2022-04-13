from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'select_sex') # отображается на главной субкатегорий 
    list_filter = ('subcategory', 'select_sex',) # фильтр по категориям, по полу 
    prepopulated_fields = {'slug': ('name',)} # дублируется с name в slug 