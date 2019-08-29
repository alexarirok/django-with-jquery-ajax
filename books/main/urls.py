from django.conf.urls import url
from main import views
from django.urls import path, include

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('base/', views.base, name='base'),
    url(r'^main/create/$', views.book_create, name='book_create'),
    url(r'^main/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^main/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
]

