from django.urls import path
from .views import PostsHomePage

urlpatterns = [
    path("messages/", PostsHomePage.as_view(), name="posts_home")
]