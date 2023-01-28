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
    publisher_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Publisher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.publisher_name = validated_data.get('publisher_name',instance.publisher_name)
        instance.phone_number = validated_data.get('phone_number',instance.phone_number)

