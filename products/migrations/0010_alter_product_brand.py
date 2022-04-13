# Generated by Django 3.2.10 on 2022-04-12 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_brands'),
        ('products', '0009_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='categories.brands'),
            preserve_default=False,
        ),
    ]
