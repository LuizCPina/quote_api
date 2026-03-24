from django.urls import path
from .views import QuoteListCreate

urlpatterns = [
    path('quotes/', QuoteListCreate.as_view(), name='quote-list-create'),
]
