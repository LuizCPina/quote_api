from django.urls import path
from .views import QuoteDetailView, QuoteListCreate, QuoteRandomView

urlpatterns = [
    path('quotes/', QuoteListCreate.as_view(), name='quote-list-create'),
    path('quotes/random/', QuoteRandomView.as_view(), name='quote-random'),
    path('quotes/<int:id>/', QuoteDetailView.as_view(), name='quote-detail'),
]
