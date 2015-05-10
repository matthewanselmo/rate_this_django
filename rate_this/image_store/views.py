from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import UserImageForm


def index(request):
    return render_to_response('image_store/index.html')


def uploadImage(request):
    context = RequestContext(request)

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

    return render_to_response('image_store/upload_image.html', {
        'user_image_form': user_image_form}, context)
