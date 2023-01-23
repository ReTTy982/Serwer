from django.contrib import admin
import traceback
from django.db import connection
from .models import *

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)

# Register your models here.


#if Book.objects.count() == 0:
#    print("Populating db")
#    try:
#        with open("data/populate.sql") as file:
#            create_query = file.read()
#
#        with connection.cursor() as cursor:
#            cursor.execute(create_query)
#    
#    except:
#        print(traceback.format_exc())
#
