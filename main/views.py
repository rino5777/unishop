from django.shortcuts import render
from django.http import request
# Create your views here.
def main(request):
    return render (request, 'main/main_page.html')
