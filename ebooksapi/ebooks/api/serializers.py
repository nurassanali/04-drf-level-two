from rest_framework import serializers
from ebooks.models import Review, Ebook

class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    exclude = ("ebook",)

class EbookSerializer(serializers.ModelSerializer):
  reviews = ReviewSerializer(many=True, read_only=True)
  
  class Meta:
    model = Ebook
    fields = "__all__"