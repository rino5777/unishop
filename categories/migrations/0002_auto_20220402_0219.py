# Generated by Django 3.2.10 on 2022-04-01 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='text',
            field=models.TextField(default=0, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
