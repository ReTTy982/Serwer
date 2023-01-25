from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse,HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .models import *
import base64
import csv
import random
import datetime
from datetime import timedelta
# Create your views here.

@csrf_exempt
def test(request: HttpRequest):
    if request.user.is_authenticated:
        print("TAK")
    params = request.headers["Authorization"].split(" ")
    text = params[1]
    print(base64.urlsafe_b64decode(text))
    print(params)
    try:
        publisher = Publisher.objects.values().get(publisher_name='Cos')
    except Publisher.DoesNotExist:
        print("unlucky")
    to_add = Publisher(publisher_name="Kawka", phone_number="4654")
    to_add.save()
    branch = Branch.objects.create(branch_address = "Inflancka")
    response = JsonResponse(Publisher.objects.values().get(publisher_name="Kawka"))
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
        print(params)
        text = params[1]
        
        encoded =base64.urlsafe_b64decode(text)
        x = encoded.decode('UTF-8')
        print(x)
        x = x.split(':')
        username = x[1]
        password = x[0]
        user = authenticate(username=username, password=password)
        if user is not None:
            print(user)
            login(request,user)
            print("TAK")
            print(request.session)
        #print(x[1])
        
        
        #user= authenticate(username=encoded[0],password=encoded[1])
        #print(user)
    return HttpResponse(request.session)

def populate(request):
    
    with open('data/branch.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:

            Branch.objects.create(branch_address=','.join(row))

    with open('data/publisher.csv', newline='') as c:
        reader = csv.reader(c, delimiter=';', quotechar='|')
        first_row=True
        for row in reader:

            Publisher.objects.create(publisher_name = row[0],phone_number=row[1])
            
    with open('data/author.csv', newline='') as c:
        reader = csv.reader(c, delimiter=';', quotechar='|')

        for row in reader:

            Author.objects.create(author_name = row[0])
            
    
    with open('data/book.csv', newline='') as c:
        reader = csv.reader(c, delimiter=';', quotechar='|')
        publishers =Publisher.objects.values()
        authors = Author.objects.values()
        for row in reader:

            
            publisher = Publisher.objects.get(publisher_name = random.choice(publishers)["publisher_name"])

            author = Author.objects.get(id = random.choice(authors)["id"])
            
            Book.objects.create(book_title=row[0],publisher_name=publisher,author=author,category=row[1])
            
    
    books = Book.objects.values()
    branches = Branch.objects.values()

    for i in range(10000):
        book = Book.objects.get(id=random.choice(books)["id"])
        branch = Branch.objects.get(id=random.choice(branches)["id"])
        BookCopy.objects.create(book=book,branch=branch)

    
    numbers = [] 
    for i in range(10000,99999):
        numbers.append(i)
    with open('data/user.csv', newline='') as c:
        reader = csv.reader(c, delimiter=';', quotechar='|')

        for row in reader:
            card = random.choice(numbers)
            numbers.remove(card)
            
            LibraryUser.objects.create(first_name=row[0],last_name=row[1],card_number=card,login=row[2],password=row[3],address=row[4],phone_number=row[5])
            user = User.objects.create_user(
            username=row[2],
            password=row[3]
            )
            user.save()
        
    branches = Branch.objects.values()
    with open('data/librarian.csv', newline='') as c:
        reader = csv.reader(c, delimiter=';', quotechar='|')
        for row in reader:
            branch = Branch.objects.get(id=random.choice(branches)["id"])
            Librarian.objects.create(login=row[0],password=row[1],branch=branch,first_name=row[2],last_name=row[3])
            user = User.objects.create_user(
            username=row[2],
            password=row[3]
            )
            user.save()
    
    
    users = LibraryUser.objects.filter()
    librarians = Librarian.objects.values()

    for i in range(5000):
        librarian = Librarian.objects.get(id=random.choice(librarians)["id"])
        branch = Branch.objects.get(id=librarian.id)
        copy = BookCopy.objects.filter(branch = branch.id)
        
        for i in range(len(copy)):
            good_copy = copy[i]
            if good_copy.copy_status == 'na stanie':
                good_copy.copy_status = 'wypozyczone'
                good_copy.save()
                break
        
        user = random.choice(users)
        start_time = datetime.datetime.now() - datetime.timedelta(20)
        if bool(random.getrandbits(1)):
            end_time = datetime.datetime.now() + datetime.timedelta(20)
        else:
            end_time = datetime.datetime.now() + datetime.timedelta(60)

        BookIssue.objects.create(copy=good_copy,branch=branch,library_user=user,date_issue=start_time.date(),date_due=end_time.date(),librarian=librarian)
        

    return HttpResponse()

def issue_book(request):
    if request.method == 'POST':
        pass
@csrf_exempt
def search_book(request):
    if request.method == 'POST':
        print(BookCopy.objects.filter(branch=request.POST.get('branch')).values())
        return HttpResponse(BookCopy.objects.filter(branch=request.POST.get('branch')).values())
    else:
        return HttpRequest("Zly request")


@csrf_exempt
def search_my_books(request):
    if request.user.is_authenticated:
        user = LibraryUser.objects.get(login = request.user)
        borrowed_books = BookIssue.objects.filter(library_user=user.id)
        response = {"book_title":[],"branch":[],"date_issue":[],"date_due":[]}
        for i in range(len(borrowed_books)):
            print(borrowed_books[i].copy.book.book_title)
            response["book_title"].append(borrowed_books[i].copy.book.book_title)
            response["branch"].append(borrowed_books[i].branch.id)
            response["date_issue"].append(borrowed_books[i].date_issue.date())
            response["date_due"].append(borrowed_books[i].date_due.date())
      
    return JsonResponse(response)



