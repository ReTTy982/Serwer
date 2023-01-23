from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse,HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .models import *
import base64
# Create your views here.

@csrf_exempt
def test(request: HttpRequest):
    if request.user.is_authenticated:
        print("TAK")
    params = request.headers["Authorization"].split(" ")
    text = params[1]
    print(base64.urlsafe_b64decode(text))
    print(params)
    publisher = Publisher.objects.values().get(publisher_name='Cos')
    response = JsonResponse(publisher)
    print(type(params))
    return response



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
        #__import__('pdb').set_trace()
        user = User.objects.create_user(
            username=params.get('username'),
            password=params.get('password')
            )
        user.save()
    response = HttpResponse('TEST')
    return response

@csrf_exempt
def my_login(request):
    if request.method == 'POST':
        params = request.headers["Authorization"].split(" ")
        text = params[1]
        
        encoded =base64.urlsafe_b64decode(text)
        x = encoded.decode('UTF-8')
        print(x.split(':'))
        print(x[1])
        
        
        #user= authenticate(username=encoded[0],password=encoded[1])
        #print(user)
    return HttpResponse("OK")