from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("comic", views.ComicViewSet)
router.register("character", views.CharacterViewSet)
router.register("creator", views.CreatorViewSet)
router.register("story", views.StoryViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
