from django.urls import path
from quotes.api.views import QuoteDetailAPIView, QuoteListCreateAPIView

urlpatterns = [
  path("quote/", QuoteListCreateAPIView.as_view(), name="quote-list"),
  path("quote/<int:pk>", QuoteDetailAPIView.as_view(), name="quote-detai")
]