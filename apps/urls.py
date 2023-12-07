from django.urls import path
from apps.views import post, post_new, post_detail

app_name = "apps"

urlpatterns = [
    path("post/", post, name="post"),
    path("post/new/", post_new, name="post_new"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
]
