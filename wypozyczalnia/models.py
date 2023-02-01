from django.db import models
from django.core.validators import MinLengthValidator


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100,primary_key=True,validators=[MinLengthValidator(3)])
    phone_number = models.CharField(max_length=30,unique=True,validators=[MinLengthValidator(3)])
    class Meta:
        db_table = 'Publisher'
    
class Book(models.Model):
    book_title = models.CharField(max_length=200,validators=[MinLengthValidator(3)])
    publisher_name = models.ForeignKey('Publisher',on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.CharField(max_length=100,blank=False,validators=[MinLengthValidator(3)])
    class Meta:
        db_table = 'Book'


    
class BookCopy(models.Model):
    book = models.ForeignKey('Book',on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    copy_status = models.CharField(max_length=30,default='na stanie',validators=[MinLengthValidator(3)])
    class Meta:
        db_table = 'BookCopy'


class BookIssue(models.Model):
    copy = models.ForeignKey('BookCopy',on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    library_user = models.ForeignKey('LibraryUser', on_delete=models.CASCADE)
    date_issue = models.DateTimeField()
    date_due = models.DateTimeField()
    librarian = models.ForeignKey('Librarian', on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)
    class Meta:
        db_table = 'BookIssue'

    

class Branch(models.Model):
    branch_address = models.CharField(max_length=50,validators=[MinLengthValidator(3)])
    class Meta:
        db_table = 'Branch'
    


class Librarian(models.Model):
    login = models.CharField(max_length=20,unique=True,validators=[MinLengthValidator(3)])
    password = models.CharField(max_length=20,validators=[MinLengthValidator(3)])
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255,validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=255,validators=[MinLengthValidator(3)])
    class Meta:
        db_table = 'Librarian'
    


class LibraryUser(models.Model):
    #user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30,validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=30,validators=[MinLengthValidator(3)])
    card_number = models.IntegerField(unique=True)
    login = models.CharField(max_length=30, unique=True,validators=[MinLengthValidator(3)])
    password = models.CharField(max_length=30,validators=[MinLengthValidator(3)])
    address = models.CharField(max_length=255,validators=[MinLengthValidator(3)])
    phone_number = models.CharField(max_length=30,unique=True,validators=[MinLengthValidator(3)])
    class Meta:
        db_table = 'LibraryUser'


class Author(models.Model):
    #author_id = models.IntegerField(primary_key=True)
    author_name = models.CharField(max_length=255,validators=[MinLengthValidator(3)])
    class Meta:
        db_table = 'Author'

class Test(models.Model):
    it = models.IntegerField(primary_key=True)
    

