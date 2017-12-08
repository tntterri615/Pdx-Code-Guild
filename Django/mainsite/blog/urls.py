from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logoutUser/$', views.logoutUser, name='logoutUser'),
    url(r'^createBlog/$', views.createBlog, name='createBlog'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^blogComment/$', views.blogComment, name='blogComment'),
    url(r'^post/(?P<post_id>\d+)/$', views.detail, name='detail')
]




