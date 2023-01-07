from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.


def test(request):
    print(request.GET)
    publisher = Publisher.objects.get(publisher_name='Cos')
    #publisher.remove()
    print(publisher)
    return render(request, 'test.html')



def register(response):
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('/wypozyczalnia/test')
    else:
        form = UserCreationForm()
    return render(response, 'wypozyczalnia/register.html',{"form":form})

@csrf_exempt
def my_register(request):
    if request.method == 'POST':
        params = request.POST
        print(params)
        user = User.objects.create_user(
            username=params.get('username'),
            password=params.get('password')
            )
        user.save()
    response = HttpResponse('TEST')
    return response

