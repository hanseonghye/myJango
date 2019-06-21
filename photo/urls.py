from django.urls import path
from blog.views import *
from photo.models import Album, Photo
from photo.views import AlbumLV, AlbumDV, PhotoDV

app_name = "photo"

urlpatterns = [
    # /
    path('', AlbumLV.as_view(), name='index'),

    # /album/
    path('album/', AlbumLV.as_view(), name='album_list'),

    # /album/1
    path('<id>/', AlbumDV.as_view(), name='album_dateil'),

    # /photo/1
    path('photo/<id>', PhotoDV.as_view(), name='photo_dateil'),
]
