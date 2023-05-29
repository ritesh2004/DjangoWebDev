from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Books
from .serializers import ItemSerializers
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def showAPI(request):
    if request.method == 'GET':
        allbooks = Books.objects.all()
        serializer = ItemSerializers(allbooks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)
        