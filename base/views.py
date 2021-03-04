from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from . import serializers
from .serializers import (
    ComicSerializer,
    CreatorSerializer,
    CharacterSerializer,
    StorySerializer,
)
from . import models
from .models import Comic, Creator, Character, Story


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


class StoryByComicView(APIView):
    def get(self, request, pk):
        try:
            comic = Comic.objects.get(pk=pk)
            stories = comic.stories.all()
            serializer = StorySerializer(stories, many=True)
            return Response(serializer.data)
        except Comic.DoesNotExist:
            raise Http404


class CharacterByComicView(APIView):
    def get(self, request, pk):
        try:
            comic = Comic.objects.get(pk=pk)
            stories_in_comic = comic.stories.all().select_related("character")
            characters = set([x.character for x in stories_in_comic])
            serializer = CharacterSerializer(characters, many=True)
            return Response(serializer.data)
        except Comic.DoesNotExist:
            raise Http404
