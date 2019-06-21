from msilib.schema import ListView

from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from photo.models import Album, Photo


class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo