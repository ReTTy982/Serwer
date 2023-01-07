# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Author(models.Model):
    authorid = models.AutoField(db_column='AuthorID', primary_key=True)  # Field name made lowercase.
    authorname = models.CharField(db_column='AuthorName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    bookid = models.AutoField(db_column='BookID', primary_key=True)  # Field name made lowercase.
    booktitle = models.CharField(db_column='BookTitle', max_length=200)  # Field name made lowercase.
    publishername = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='PublisherName')  # Field name made lowercase.
    authorid = models.ForeignKey(Author, models.DO_NOTHING, db_column='AuthorID')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class Bookcopy(models.Model):
    copyid = models.AutoField(db_column='CopyID', primary_key=True)  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.
    branchid = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchID')  # Field name made lowercase.
    copystatus = models.CharField(db_column='CopyStatus', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bookcopy'


class Bookissue(models.Model):
    bookissueid = models.AutoField(db_column='bookIssueID', primary_key=True)  # Field name made lowercase.
    copyid = models.OneToOneField(Bookcopy, models.DO_NOTHING, db_column='CopyID')  # Field name made lowercase.
    branchid = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchID')  # Field name made lowercase.
    cardnumber = models.ForeignKey('User', models.DO_NOTHING, db_column='CardNumber')  # Field name made lowercase.
    dateissue = models.DateField(db_column='DateIssue')  # Field name made lowercase.
    datedue = models.DateField(db_column='DateDue')  # Field name made lowercase.
    librarianid = models.ForeignKey('Librarian', models.DO_NOTHING, db_column='LibrarianID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bookissue'


class Branch(models.Model):
    branchid = models.AutoField(db_column='BranchID', primary_key=True)  # Field name made lowercase.
    branchaddress = models.CharField(db_column='BranchAddress', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branch'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Librarian(models.Model):
    librarianid = models.AutoField(db_column='LibrarianID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    branchid = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchID')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'librarian'


class Publisher(models.Model):
    publishername = models.CharField(db_column='PublisherName', primary_key=True, max_length=100)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', unique=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publisher'


class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    cardnumber = models.IntegerField(db_column='CardNumber', unique=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', unique=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class WypozyczalniaAuthor(models.Model):
    authorid = models.IntegerField(db_column='AuthorID', primary_key=True)  # Field name made lowercase.
    authorname = models.CharField(db_column='AuthorName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wypozyczalnia_author'


class WypozyczalniaPublisher(models.Model):
    publishername = models.CharField(db_column='PublisherName', primary_key=True, max_length=100)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wypozyczalnia_publisher'
