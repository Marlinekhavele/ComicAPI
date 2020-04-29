from rest_framework import serializers
from .models import Comic, Story, Creator, Character


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = (
            "id",
            "title",
            "issue",
            "image",
            "date_published",
            "price",
            "pages",
            "created_at",
            "updated_at",
        )
            


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            "id",
            "name",
            "description",
            "image",
            "created_at",
            "updated_at",
        )


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = (
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        )


class StorySerializer(serializers.ModelSerializer):
    creator = CreatorSerializer()
    comic = ComicSerializer()
    character = CharacterSerializer()

    class Meta:
        model = Story
        fields = (
            "id",
            "title",
            "creator",
            "comic",
            "character",
            "created_at",
            "updated_at",
        )
