from rest_framework import serializers
from .models import Books

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'