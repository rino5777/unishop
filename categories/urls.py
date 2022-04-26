from django.urls import path 
from . import views

app_name = 'categories'


urlpatterns = [
    #path('')
    path('<slug:category_slug>/<slug:subcategory_slug>/', views.shopGreedLs, name  = 'shoplist'   ),
    path('categories/', views.categories, name = 'categories' ),

    #path('<category_slug>/', views.cat_product, name  = 'CategoryProduct'   ), #!!!

    path('<brand_slug>/', views.brands, name  = 'brands'   ),
    path('/<slug:subcategory_slug>/<slug>/<id>', views.productPage, name = 'product' ),

    # переход с категории и отображение сразу товара ( игнорируя субкатегории  )
    path('<slug:category_slug>', views.filters, name = 'FromCategoryToProduct' ),
    #переходим по фильрам (субкатегории )
    path('<slug:filter_slug>', views.filters, name = 'FromCategoryToSubcategory' ), 
    
]