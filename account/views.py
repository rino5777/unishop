from django.shortcuts import redirect, render
from django.http import request
from .forms import UserRegistrationForm, UserCreationForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import time
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def account(request):
    return render (request, 'user/account-profile.html')




def authorization(request):
     # Создаём форму
    form = UserRegistrationForm(request.POST)
    data = {}
    if request.method == 'POST':
        
        # Валидация данных из формы
        if form.is_valid():
            form.save()
            form.changed_data
            time.sleep(1)
            # Рендаринг страницы
            return render(request, 'user/account-profile.html',  { 'form':form } )
    else: # Иначе
        
        return render(request, 'user/account-login.html',{ 'form':form } ,)
    return render(request, 'user/account-login.html',{ 'form':form })




