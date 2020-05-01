from django.test import TestCase
import uuid
import datetime
from base.models import Comic, Character, Creator, Story


class ComicTest(TestCase):
    """ Test module for comic model """

    def setUp(self):
        Comic.objects.create(
            title='Deadpool',
            issue="1 edition",
            image='https://m.media-amazon.com/images/I/51vCE8RCEoL.jpg',
            date_published=str(datetime.datetime.now()),
            price='22.83', pages=76)
        Comic.objects.create(
            title='Harleen',
            issue="1 Edition",
            image='https://m.media-amazon.com/images/I/51vCE8RCEoL.jpg',
            price='22.83', pages=76)

    def test_comic(self):
        comic_Deadpool = Comic.objects.get(title='Deadpool')
        comic_Harleen = Comic.objects.get(title='Harleen')
        self.assertEqual(str(comic_Deadpool.title), "Deadpool")
        self.assertEqual(str(comic_Harleen.title), "Harleen")


class CharacterTest(TestCase):
    """ Test module for character model """

    def setUp(self):
        Character.objects.create(
            name='Deadpool',
            image='https://m.media-amazon.com/images/I/51vCE8RCEoL.jpg',
            description="Hello"
        )
        Character.objects.create(
            name='Deadpool2',
            image='https://m.media-amazon.com/images/I/51vCE8RCEoL.jpg',
            description="Hello test")

    def test_character(self):
        character_Deadpool = Character.objects.get(name='Deadpool')
        character_Deadpool2 = Character.objects.get(name='Deadpool2')
        self.assertEqual(str(character_Deadpool.name), "Deadpool")
        self.assertEqual(str(character_Deadpool2.name), "Deadpool2")


class CreatorTest(TestCase):
    """ Test module for creator model """

    def setUp(self):
        Creator.objects.create(
            name='Deadpool',
            description="Hello"
        )
        Creator.objects.create(
            name='Deadpool2',
            description="Hello test")

    def test_creator(self):
        creator_Deadpool = Creator.objects.get(name='Deadpool')
        creator_Deadpool2 = Creator.objects.get(name='Deadpool2')
        self.assertEqual(str(creator_Deadpool.name), "Deadpool")
        self.assertEqual(str(creator_Deadpool2.name), "Deadpool2")


# class StoryTest(TestCase):
#     """ Test module for story model """

#     def setUp(self):
#         Story.objects.create(
#             title='Deadpool',
#             comic_id=str(uuid.uuid4()),
#             creator_id=str(uuid.uuid4()),
#             character_id=str(uuid.uuid4())
#         )
#         Story.objects.create(
#             title='Deadpool',
#             comic_id=str(uuid.uuid4()),
#             creator_id=str(uuid.uuid4()),
#             character_id=str(uuid.uuid4()))

#     def test_story(self):
#         story_Deadpool = Story.objects.get(title='Deadpool')
#         story_Deadpool2 = Story.objects.get(title='Deadpool2')
#         self.assertEqual(str(story_Deadpool.title), "Deadpool")
#         self.assertEqual(str(story_Deadpool2.title), "Deadpool2")
