from rest_framework import serializers
from wypozyczalnia.models import *
from drf_queryfields import QueryFieldsMixin


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    
class BookSerializer(DynamicFieldsModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,slug_field='author_name')
    class Meta:
        model = Book
        fields = ['id','book_title','publisher_name','author','category']
    

class AuthorSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Author
        fields = ['id','author_name']

class PublisherSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Publisher
        fields = ['publisher_name','phone_number']

class BookCopySerializer(DynamicFieldsModelSerializer):
    book = serializers.SlugRelatedField(read_only=True,slug_field='book_title')
    branch = serializers.SlugRelatedField(read_only=True,slug_field='branch_address')
    author = serializers.SerializerMethodField("get_author")
    publisher = serializers.SerializerMethodField("get_publisher")
    
    
    class Meta:
        model = BookCopy
        fields = ['id','book','author','publisher','branch','copy_status',]

    # def create(self,validated_data):
    #     print(f"KEK{validated_data}")
    #     book = Book.objects.get(validated_data['book_id'])
    #     branch = Branch.objects.get(validated_data['branch_id'])
    #     return BookCopy.objects.create(book=book,branch=branch)

    def get_author(self,obj):
        return obj.book.author.author_name
    def get_publisher(self,obj):
        return obj.book.publisher_name.publisher_name


class BookIssueSerializer(DynamicFieldsModelSerializer):
    branch = serializers.SlugRelatedField(read_only=True,slug_field='branch_address')
    library_user = serializers.SlugRelatedField(read_only=True,slug_field='card_number')
    class Meta:
        model = BookIssue
        fields = ['id','copy','branch','library_user','date_issue','date_due','librarian','returned']

class BranchSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Branch
        fields = ['id','branch_address']

class LibrarianSerializer(DynamicFieldsModelSerializer):
    branch = serializers.SlugRelatedField(read_only=True,slug_field='branch_address')
    class Meta:
        model = Librarian
        fields = ['id','login','password','branch','first_name','last_name']

class LibraryUserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = LibraryUser
        fields = ['id','first_name','last_name','card_number','login','password','address','phone_number']
