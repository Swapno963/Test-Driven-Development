from .views import index,post_detail
from django.urls import path

urlpatterns = [
    path("", index, name="homepage"),
    path("post/<int:id>", post_detail, name="post_detail"),
    ]
