from django.shortcuts import render
from .serializers import QuoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quote

class QuoteListCreate(APIView):

    def get(self, request):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = QuoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)     
        
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST) 

class QuoteRandomView(APIView):

    def get(self, request):
        quote = Quote.objects.order_by('?').first()
        

        if quote:
            serializer = QuoteSerializer(quote)
            return Response(serializer.data, status.HTTP_200_OK)
        
        else:
            return Response({'error': 'No quotes available'}, status.HTTP_404_NOT_FOUND)