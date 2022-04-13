from django.urls import path 
from . import views

app_name = 'account'


urlpatterns = [

    path('', views.account, name = 'account' ),  # главная  account-login.html

    path('authorization', views.authorization, name = 'authorization' ),
    
]