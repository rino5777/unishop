from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, SubCategory, Brands
from django.http import HttpResponse
from products.models import Product
from django.core.paginator import Paginator
# Create your views here.






def categories(request, category_slug = None ):
    category = None
    main_cat = Category.objects.all()
    subcategories = SubCategory.objects.filter()
    

    if category_slug:                                                 # фильтрация субкатегорий по категориям 
        category = get_object_or_404(Category, slug=category_slug)    # 
        subcategories = subcategories.filter(category = category)     #
        
    return render (request,  'shop-categories/shop-categories.html', { 'elements_main': main_cat,  'subcategories': subcategories, })





def cat_product(request, category_slug = None ): # переход на другую страницу со всеми подкатегориями которые входят а категорию 
    category = None
    sub = None
    main_cat = Category.objects.all()
    subcategories = SubCategory.objects.filter()
    products = Product.objects.all()
    

    if category_slug:                                                 # фильтрация субкатегорий по категориям 
        category = get_object_or_404(Category, slug=category_slug)    # 
        subcategories = subcategories.filter(category = category)
       
    return render (request,  'shop-categories/shop_grid_ls.html', {  'elements_main': main_cat,  'subcategories': subcategories, 'sub': sub, 'products':products })




def productPage( request,  id, slug, subcategory_slug  ):

    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
    all_str = get_list_or_404(Product, id = id, slug = slug  )
    return render( request, 'shop-categories/shop-single.html', {'all_str': all_str })





def shopGreedLs(request, category_slug = None, subcategory_slug = None):

    #productsub = SubCategory.objects.all()
    subcategory = None
    main_sub = SubCategory.objects.all()
    product = Product.objects.filter()
    #повторяю левый фильтр из filters ( сделать отельную функцию для фильтра  )
    main_cat = Category.objects.all()
    subcategories = SubCategory.objects.filter()
    filter_left = {}
    for type_c in subcategories:
        for i in range(len(main_cat)):
            if type_c.category == main_cat[i]:
                filter_left[type_c] = main_cat[i]

    
    if subcategory_slug:
        category = get_object_or_404(Category, slug=category_slug)         # фильтрация товара  по субкатегориям  
        subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)    # 
        product = product.filter(subcategory = subcategory)     # фильтруем товар 
        
    return  render (request, 'shop-categories/shop_grid_ls.html', {'product': product,  'main_sub': main_sub, 'filter_left':filter_left, 'main_cat':main_cat })


def productPage(request, subcategory_slug, slug, id): # отображение страницы товара (  )
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
    product = get_object_or_404(Product, slug=slug, id = id)
    #return  HttpResponse("hello!")
    return  render (request, 'shop-categories/shop-single.html', {'product': product,})



#------------------------------------------------------------------------------------------

def filters(request, category_slug = None, filter_slug = None):
    category = None
    subcategory = None
    main_cat = Category.objects.all()
    main_sub = SubCategory.objects.all()

    subcategories = SubCategory.objects.filter()
    product = Product.objects.filter()
    all_str = get_list_or_404(Product)
    l_p = []   #  список продуктов
    filter_left = {}
 

    for type_c in subcategories:
        for i in range(len(main_cat)):
            if type_c.category == main_cat[i]:
                filter_left[type_c] = main_cat[i]
                #print(type_c, '/', type_c.category, '/ категория /', main_cat[i] ) #вывод подкатегорий в категориях 
    print(filter_left)

    if filter_slug:      
        category = get_object_or_404(subcategory, slug=filter_slug)  # фильтрация товара  по субкатегориям  
        subcategories = subcategories.filter(category = category)


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)  # фильтрация товара  по субкатегориям  
        subcategories = subcategories.filter(category = category)   # 
       

        for i in subcategories:     # фильтруем товар 
            for q in all_str:
                if i == q.subcategory:
                    l_p.append(q) # добавление продуктов 
        #print(l_p)
    #set up pagination
    paginator = Paginator(l_p, 2)
    page = request.GET.get('page')
    list_product = paginator.get_page(page)
    numofpage = 'a' * list_product.paginator.num_pages

    return render(request,  'shop-categories/shop_grid_ls.html', { 'productS':all_str,
                             'filetBySubcategory': subcategories, 'l_p':l_p, 'main_sub': main_sub,
                             'main_cat':main_cat, 'list_product': list_product, 'numofpage': numofpage, 'filter_left': filter_left } )
    








def brands(request, brand_slug = None):
    bb = Brands.objects.all()
    product = Product.objects.filter()

    if brand_slug:
        brand = get_object_or_404(Brands, slug=brand_slug)    # 
        brend_b_product = product.filter(brand = brand)

    return render (request,  'shop-categories/shop_grid_ls.html', { 'brend_b_product': brend_b_product, 'bb':bb })