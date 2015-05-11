"""rate_this URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns

from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from django.conf import settings
from django.conf.urls.static import static


# Create a new class that redirects the user to the index page,
# if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/'

urlpatterns = [
    url(r'^', include('image_store.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^posts/', include('image_store.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += patterns('',
#     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),)
