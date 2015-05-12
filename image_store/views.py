from django.shortcuts import render

from .forms import UserImageForm
from .models import UserImage


def index(request):
    return render(request, 'image_store/index.html')


def explore(request, page=0):

    low = int(page) * 9
    high = low + 9

    posts = UserImage.objects.all().order_by('-created')[low:high]

    next_page = int(page) + 1
    prev_page = int(page) - 1
    return render(request, 'image_store/explore.html', {'posts': posts,
                  'next_page': next_page, 'prev_page': prev_page})


def post(request):

    if request.method == 'POST':
        user_image_form = UserImageForm(request.POST, request.FILES)

        if user_image_form.is_valid():
            user_image = user_image_form.save(commit=False)
            user_image.user = request.user
            user_image.save()

            return index(request)
        else:
            print(user_image_form.errors)
    else:
        user_image_form = UserImageForm()

    return render(request, 'image_store/upload_image.html', {
        'user_image_form': user_image_form})
