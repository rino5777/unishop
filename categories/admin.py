from django.contrib import admin
from .models import Category, SubCategory, Brands

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category') # отображается на главной субкатегорий 
    list_filter = ('category',) # фильтр по категориям 
    prepopulated_fields = {'slug': ('name',)} # дублируется с name в slug 


admin.site.register(Brands)



# @admin.register(SexCategory)
# class SexCategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name',)}
