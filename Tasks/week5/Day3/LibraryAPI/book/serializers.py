from book.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = "__all__"

    # id = serializers.IntegerField(read_only = True)
    # title = serializers.CharField(max_length = 70)
    # author = serializers.CharField(max_length = 50)
    # isbn = serializers.IntegerField()

    # def create (self, validated_data):
    #     print(f"validated_data: {validated_data}")
    #     print(f"**Validated data: {validated_data}")
    #     return Book.objects.create(**validated_data)
    
    # def update (self, instance, validated_data):
    #     '''
    #     Update an existing object
            
    #         Args:
    #             self, which refers to the serializer instance, 
    #             instance, which is the existing Book instance to be updated,
    #             validated_data, which is a dictionary containing the new data to update the instance.

    #         Returns:  
    #             he updated instance after all the modifications and changes have been made.
    #     '''
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.isbn = validated_data.get('isbn', instance.isbn)
    #     instance.save()
    #     return instance
    
    # def delete(self, instance):
    #     pass

    
