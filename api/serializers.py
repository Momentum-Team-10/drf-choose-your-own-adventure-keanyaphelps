from rest_framework import serializers
from ..core.models import Book, User

class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

class Meta:
    model = Book
    fields = ('title', 'author', 'publication_date', 'publisher', 'genre', 'featured', 'owner',)

    