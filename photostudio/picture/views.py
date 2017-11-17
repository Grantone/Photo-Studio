from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    posts = Post.get_posts()

    return render(request, 'all-posts/index.html', {"posts": posts})


def post(request, post_id):

    try:
        post = Post.objects.get(id=post_id)
        tags = post.tags.all()

    except DoesNotExist:
        raise Http404()

    return render(request, 'all-posts/post.html', {"post": post, "tags": tags})


def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-posts/search.html', {"message": message, "posts": searched_posts})
