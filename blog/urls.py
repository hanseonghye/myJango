from django.urls import path
from blog.views import *

urlpatterns = [
    # /
    path('', PostLV.as_view(), name='index'),
    # /post/
    path('post/', PostLV.as_view(), name='post_list'),
    # /post/django-example/
    path('post/<slug>/', PostDV.as_view(), name='post_detail'),
    # /archive/
    path('archive/', PostAV.as_view(), name='post_archive'),
    # /[year]/
    path('<year>/$', PostYAV.as_view(), name='post_year_archive'),
]
