from django.db import models
from django.urls import reverse

# Create your models here.


class Brands(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering =('name',)

    def get_absolute_url(self):
        return reverse('categories:Brands', args = [ self.slug ])



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    text = models.TextField(max_length=50, unique=True)
   

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categoryes'
        ordering =('name',)

    def get_absolute_url(self):
        return reverse('categories:FromCategoryToProduct', args = [self.slug ] ) #'categories:CategoryProduct'


    def __str__(self):
        return str(self.name)


class SubCategory(models.Model):
    MEN = 'M'
    WOOMENS = 'W'
    CHILD = 'C'
    
    SEX = [
        (MEN, 'MEN'),
        (WOOMENS, 'WOOMENS'),
        (CHILD, 'CHILD')
        
    ]

    name = models.CharField(max_length=100, unique =True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
   
    #select_sex = models.CharField(max_length=5, choices= SEX,
        #default= MEN)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategoryes'
        ordering =('name',)

    def get_absolute_url(self):
        return reverse('categories:shoplist', args=[self.category.slug, self.slug])

    # def get_product_url(self):
    #     return reverse('categories:productlist',)


