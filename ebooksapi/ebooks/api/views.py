from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from ebooks.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly

class EbookListCreateAPIView(generics.ListCreateAPIView):
  queryset = Ebook.objects.all()
  serializer_class = EbookSerializer
  permission_classes = [IsAdminUserOrReadOnly]

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Ebook.objects.all()
  serializer_class = EbookSerializer
  permission_classes = [IsAdminUserOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):
  queryset = Ebook.objects.all()
  serializer_class = ReviewSerializer

  def perform_create(self, serializer):
    ebook_pk = self.kwargs.get("ebook_pk")
    ebook = get_object_or_404(Ebook, pk=ebook_pk)
    review_author = self.request.user
    review_queryset = Review.objects.filter(ebook=ebook, 
                                            review_author=review_author)
    if review_queryset.exists():
      raise ValidationError("You have already reviewed this ebook.")
    serializer.save(ebook=ebook, review_author=review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  permission_classes = [IsReviewAuthorOrReadOnly]