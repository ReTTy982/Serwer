from django.db import models


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30,unique=True)
    class Meta:
        db_table = 'Publisher'
    
"""
class Book(models.Model):
    #book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=200)
    publisher_name = models.ForeignKey('Publisher',on_delete=models.CASCADE)
    author_id = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    class Meta:
        db_table = 'Book'
    def __str__(self):
        return f"{self.book_title}, {self.author_id.author_name}"

    


class BookCopy(models.Model):
    copy_id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey('Book',on_delete=models.CASCADE)
    branch_id = models.ForeignKey('Branch', on_delete=models.CASCADE)
    copy_status = models.CharField(max_length=30,default='na stanie')
    class Meta:
        db_table = 'BookCopy'


class BookIssue(models.Model):
    book_issue_id = models.IntegerField(primary_key=True)
    copy_id = models.ForeignKey('BookCopy',on_delete=models.CASCADE)
    branch_id = models.ForeignKey('Branch', on_delete=models.CASCADE)
    card_number = models.ForeignKey('LibraryUser', on_delete=models.CASCADE)
    date_issue = models.DateTimeField()
    date_due = models.DateTimeField()
    librarian_id = models.ForeignKey('Librarian', on_delete=models.CASCADE)
    class Meta:
        db_table = 'BookIssue'

    

class Branch(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    branch_address = models.CharField(max_length=50)
    class Meta:
        db_table = 'Branch'
    


class Librarian(models.Model):
    librarian_id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    branch_id = models.ForeignKey('Branch', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    class Meta:
        db_table = 'Librarian'
    





class LibraryUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    card_number = models.IntegerField(unique=True)
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30,unique=True)
    class Meta:
        db_table = 'LibraryUser'


class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    author_name = models.CharField(max_length=255)
    class Meta:
        db_table = 'Author'
    


"""