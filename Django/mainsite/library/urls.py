from django.conf.urls import url, include
from django.contrib import admin


from . import views

app_name = 'library'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^checkin/$', views.checkin, name='checkin'),
    # url(r'^(?P<book_id>[0-9]+)/checkout/$', views.checkout, name='checkout'),
    # url(r'^(?P<book_id>[0-9]+)/checkin/$', views.checkin, name='checkin')
]