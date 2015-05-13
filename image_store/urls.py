from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.upload, name='post'),
    url(r'^post/(?P<postId>[0-9][0-9]*)/$', views.viewPost, name='upload'),
    url(r'^explore/$', views.explore, name='explore'),
    url(r'^explore/(?P<page>[0-9][0-9]*)/$', views.explore, name='explore'),
]
