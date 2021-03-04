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
            "image",
            "description",
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

        def create(self, validated_data):
            comic = Comic.objects.get(pk=validated_data["comic"])
            character = Character.objects.get(pk=validated_data["character"])
            creator = Creator.objects.get(pk=validated_data["creator"])
            story = Story.objects.create(
                comic=comic, character=character, creator=creator
            )
            return story
