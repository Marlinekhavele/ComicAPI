from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from .serializers import (
    ComicSerializer,
    CreatorSerializer,
    CharacterSerializer,
    StorySerializer,
)
from . import models


class ComicViewSet(viewsets.ModelViewSet):
    """Handles Listing comics."""

    serializer_class = serializers.ComicSerializer
    queryset = models.Comic.objects.all()


class CharacterViewSet(viewsets.ModelViewSet):
    """Handles Listing characters."""

    serializer_class = serializers.CharacterSerializer
    queryset = models.Character.objects.all()


class CreatorViewSet(viewsets.ModelViewSet):
    """Handles Listing creators."""

    serializer_class = serializers.CreatorSerializer
    queryset = models.Creator.objects.all()


class StoryViewSet(viewsets.ModelViewSet):
    """Handles Listing stories."""

    serializer_class = serializers.StorySerializer
    queryset = models.Story.objects.all()
