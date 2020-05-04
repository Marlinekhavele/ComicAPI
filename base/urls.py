from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.register("comic", views.ComicViewSet)
router.register("character", views.CharacterViewSet)
router.register("creator", views.CreatorViewSet)
router.register("story", views.StoryViewSet)
# router.register("tags", views.TagViewSet)

urlpatterns = [
    path(
        "stories-in-comic/<int:pk>/",
        views.StoryByComicView.as_view(),
        name="stories-in-comic",
    ),
    path(
        "characters-in-comic/<int:pk>/",
        views.CharacterByComicView.as_view(),
        name="characters-in-comic",
    ),
    path("", include(router.urls)),
]
