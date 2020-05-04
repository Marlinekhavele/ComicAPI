from rest_framework import serializers
from .models import Comic, Story, Creator, Character


# class TagSerializer(serializers.ModelSerializer):
#     """Tag serializer"""
#     comic = serializers.SlugRelatedField(
#         many=True,
#         read_only=True,
#         slug_field=("featured", "latest", "trending")
#     )

#     class Meta:
#         model = Tag
#         fields = ("id", "comic", "featured", "latest", "trending")


class ComicSerializer(serializers.ModelSerializer):
    # tags = serializers.SlugRelatedField(
    #     many=True,
    #     slug_field=("featured", "latest", "trending"),
    #     queryset=Tag.objects.all()
    # )

    class Meta:
        model = Comic
        fields = (
            "id",
            "title",
            # "tags",
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
    # creator = CreatorSerializer()
    # comic = ComicSerializer()
    # character = CharacterSerializer()

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
