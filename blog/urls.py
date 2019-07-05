from django.urls import path
from blog.views import *

app_name = "blog"

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
    path('<year>/', PostYAV.as_view(), name='post_year_archive'),

    # /teg/
    path('tag/', TagTV.as_view(), name='tag_cloud'),

    # /tag/tagname/
    path('tag/<atg>/', PostTOL.as_view(), name='tagged_object_list'),
    # /search/
    path('search/', SearchFormView.as_view(), name='search'),
]
