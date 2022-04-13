# Generated by Django 3.2.10 on 2022-04-02 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0006_remove_subcategory_select_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d')),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('discount', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('size', models.CharField(blank=True, max_length=200, null=True)),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('SKU', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('select_sex', models.CharField(choices=[('M', 'Men'), ('W', 'Woomen'), ('C', 'Child')], default='M', max_length=5)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='categories.subcategory')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('name',),
            },
        ),
    ]
