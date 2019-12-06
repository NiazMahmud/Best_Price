import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'index.html')


def account(request):
    return render(request, 'MyAccount.html')

def reg(request):
    return render(request, 'reg.html')


def new_search(request):
    search = request.POST.get('search')
    stuff_for_frontend = {
       'search': search,

   }
    return render(request, 'Search.html', stuff_for_frontend)