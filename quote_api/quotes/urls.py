from django.urls import path
from .views import QuoteListCreate, QuoteRandomView

urlpatterns = [
    path('quotes/', QuoteListCreate.as_view(), name='quote-list-create'),
    path('quotes/random/', QuoteRandomView.as_view(), name='quote-random'),
]
