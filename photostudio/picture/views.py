from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, tags
from django.http import Http404

# Create your views here.


def index(request):
    posts = Post.objects.all()
    tag = tags.objects.all()
    # print (posts)
    return render(request, 'all-posts/index.html', {"posts": posts, "all-tags": tag})


def post(request, post_id):

    try:
        post = Post.objects.get(pk=post_id)

    except Post.DoesNotExist:
        raise Http404()

    return render(request, 'all-posts/post.html', {"post": post})


def photos(request, photo_id):
    try:
        photo = Post.objects.get(id=photo_id)

    except Post.DoesNotExist:
        raise Http404()

    return render(request, 'all-posts/photos.html', {"photo": photo})


def tag(request, tag_id):
    # all_tags = tags.display_tags()
    try:
        tag = tags.objects.get(id=tag_id)
        photos = Post.objects.filter(tag=tag).all()

    except DoesNotExist:
        raise Http404()

    return render(request, 'all-posts/tag.html', {"tag": tag, "photos": photos})


def collections(request):

    try:
        photo = Post.objects.get(id=photo_id)

    except Post.DoesNotExist:
        raise Http404()

    return render(request, 'all-posts/collections.html', {"tag": tag, "photos": photos})


def search_results(request):
        # get all tags
    # all_tags = tags.display_tags()

    # check if photo query exists in our request.GET object
    if 'tag' in request.GET and request.GET['tag']:
        search_term = request.GET.get('tag')  # get search term
        search_tags = tags.search_for_tag(search_term)
        photo = Post.objects.filter(tags=search_tags).all()
        message = f"{search_term}"

        return render(request, 'all-posts/search.html', {"message": message, "search_tags": search_tags, "photo": photo})

    else:
        message = "You haven't searched for any term"

        return render(request, 'all-posts/search.html', {"message": message})
