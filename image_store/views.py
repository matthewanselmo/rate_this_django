from django.shortcuts import render

from .forms import PostForm, CommentForm
from .models import Post, Comment, UserUpvote


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


def viewPost(request, postId=0):
    post = Post.objects.get(id=postId)
    comments = Comment.get_comments_for_post(post)
    comment_form = CommentForm()
    can_upvote = UserUpvote.can_user_upvote(post, request.user)

    return render(request, 'image_store/post.html',
                  {'post': post, 'comments': comments,
                   'comment_form': comment_form, 'can_upvote': can_upvote})


def comment(request, postId=0):
    post = Post.objects.get(id=postId)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

    else:
        comment_form = CommentForm()

    return viewPost(request, postId)


def upvote(request, postId=0):
    _post = Post.objects.get(id=postId)

    if request.method == 'POST':
        if UserUpvote.can_user_upvote(_post, request.user):
            _post.upvotes += 1
            _post.save()

            up = UserUpvote(user=request.user, post=_post)
            up.save()

    return viewPost(request, postId)


def me(request, page=0):    

    low = int(page) * 9
    high = low + 9

    posts = Post.objects.all().filter(user_id=request.user.id).order_by('-created')[low:high]

    next_page = int(page) + 1
    prev_page = int(page) - 1
    return render(request, 'image_store/explore.html', {'posts': posts,
                  'next_page': next_page, 'prev_page': prev_page})
