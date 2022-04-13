from django.db import models
from categories.models import SubCategory, Category, Brands
from django.urls import reverse
import uuid
# Create your models here.


class Product(models.Model):

    SEX = [('MEN', 'Men'), ('WOOMEN', 'Woomen'), ('CHILD', 'Child')]
    SIZE_M_SHOES = [('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'),('44', '44') ]
    SIZE_W_SHOES = [('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'),('40', '40') ]
    
    #id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable=False, max_length=5, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=15, unique=True)
    select_sex = models.CharField(max_length=10, choices= SEX, default= 'MEN')
    size = models.CharField(max_length=200, choices= SIZE_M_SHOES, default= '40')
    #brand = models.CharField(max_length=200, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, related_name='brand', on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='photo/%Y/%m', blank=True, null=True)
    image2 = models.ImageField(upload_to='photo/%Y/%m', blank=True, null=True)
    image3 = models.ImageField(upload_to='photo/%Y/%m', blank=True, null=True)
    image4 = models.ImageField(upload_to='photo/%Y/%m', blank=True, null=True)
    image5 = models.ImageField(upload_to='photo/%Y/%m', blank=True, null=True)
    
    price = models.CharField(max_length=100, blank=True, null=True)
    discount = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    #size = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=200, blank=True, null=True)
    
    #category = models.CharField(max_length=200, blank=True, null=True)
    #subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    





    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering =('name',)

    def get_absolute_url(self):

        return reverse('categories:product', args=[ self.subcategory.slug, self.slug, self.id, ]) 