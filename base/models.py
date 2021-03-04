from django.db import models
from datetime import datetime
from decimal import Decimal
from django.utils.translation import gettext as _


# Create your models here.
class Creator(models.Model):
    """ Creator Model"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name


class Comic(models.Model):
    """ Comic Model"""
    title = models.CharField(_("Comic's title"), max_length=128)
    issue = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, editable=False)
    price = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal("0.00")
    )
    pages = models.IntegerField(_("Pages"), default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.title


class Character(models.Model):
    """ Character Model"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name


class Story(models.Model):
    """ Story Model"""
    title = models.CharField(_("Story title"), max_length=128)
    comic = models.ForeignKey(
        Comic, on_delete=models.CASCADE, related_name="stories"
    )
    creator = models.ForeignKey(
        Creator, on_delete=models.CASCADE, related_name="creator"
    )
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="character"
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.title
