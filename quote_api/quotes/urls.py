from django.urls import path
from .views import home,QuoteDetailView, quote_list_create, QuoteRandomView

urlpatterns = [    
    path('', home, name='home'),
    path('quotes/', quote_list_create, name='quote-list-create'),
    path('quotes/random/', QuoteRandomView.as_view(), name='quote-random'),
    path('quotes/<int:id>/', QuoteDetailView.as_view(), name='quote-detail'),
]
