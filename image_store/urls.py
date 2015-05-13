from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.upload, name='upload'),
    url(r'^post/(?P<postId>[0-9][0-9]*)/$', views.viewPost, name='post'),
    url(r'^comment/(?P<postId>[0-9][0-9]*)/$', views.comment, name='comment'),
    url(r'^upvote/(?P<postId>[0-9][0-9]*)/$', views.upvote, name='upvote'),
    url(r'^explore/$', views.explore, name='explore'),
    url(r'^explore/(?P<page>[0-9][0-9]*)/$', views.explore, name='explore'),
    url(r'^me/$', views.me, name='explore'),
    url(r'^me/(?P<page>[0-9][0-9]*)/$', views.me, name='me'),
]
