from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from .serializers import ComicSerializer
from . import models


class ComicViewSet(viewsets.ModelViewSet):
    """Handles Listing and Updating comics."""

    serializer_class = serializers.ComicSerializer
    queryset = models.Comic.objects.all()

