from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from .serializers import QuoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quote
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def quote_list_create(request):
    if request.method == 'GET':
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = QuoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class QuoteRandomView(APIView):

    def get(self, request):
        quote = Quote.objects.order_by('?').first()
        

        if quote:
            serializer = QuoteSerializer(quote)
            return Response(serializer.data, status.HTTP_200_OK)
        
        return Response({'error': 'No quotes available'}, status.HTTP_404_NOT_FOUND)
        

class QuoteDetailView(APIView):

    def get(self, request, id):
            quote = get_object_or_404(Quote, id=id)
            serializer = QuoteSerializer(quote)
            return Response(serializer.data, status.HTTP_200_OK)
    
def home(request):
    return render(request, 'home.html')