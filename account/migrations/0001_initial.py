# Generated by Django 3.2.10 on 2022-03-26 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank=True, max_length=200, null=True)),
                ('LastName', models.CharField(blank=True, max_length=200, null=True)),
                ('EmailAddress', models.EmailField(blank=True, max_length=500, null=True)),
                ('profile_image', models.ImageField(blank=True, default='profiles/img_avatar.png', null=True, upload_to='profiles/')),
                ('Password', models.CharField(blank=True, max_length=64, null=True)),
                ('ConfirmPassword', models.CharField(blank=True, max_length=64, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
