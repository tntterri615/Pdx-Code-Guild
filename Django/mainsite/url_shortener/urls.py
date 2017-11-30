from django.conf.urls import url

from . import views


app_name = 'url_shortener'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),                                     #pattern for submitting form
]