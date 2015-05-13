from django.shortcuts import render

from .forms import PostForm
from .models import Post


def index(request):
    return render(request, 'image_store/index.html')


def explore(request, page=0):

    low = int(page) * 9
    high = low + 9

    posts = Post.objects.all().order_by('-created')[low:high]

    next_page = int(page) + 1
    prev_page = int(page) - 1
    return render(request, 'image_store/explore.html', {'posts': posts,
                  'next_page': next_page, 'prev_page': prev_page})


def upload(request):

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            return index(request)
        else:
            print(post_form.errors)
    else:
        post_form = PostForm()

    return render(request, 'image_store/upload.html', {
        'post_form': post_form})


def post(request, postId=0):
    post = Post.objects.get(id=postId)

    return render(request, 'image_store/post.html', {'post': post})
