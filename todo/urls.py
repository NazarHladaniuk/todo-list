from django.urls import path

from .views import (
    home,
    TagListView,
)

urlpatterns = [
    path("", home, name="home"),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
]


app_name = "todo"
