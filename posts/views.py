from django.shortcuts import render

from .models import Posts


# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, "posts/index.html", {"posts": posts})


def post_detail(request, id):
    post =Posts.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'posts/detail.html',context)