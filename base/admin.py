from django.contrib import admin
from .models import Comic, Story, Creator, Character

# Register your models here.
admin.site.register(Comic)
admin.site.register(Story)
admin.site.register(Creator)
admin.site.register(Character)