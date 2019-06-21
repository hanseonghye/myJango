from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include

from mysite import settings
from mysite.views import HomeView

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('bookmark/', include('bookmark.urls'), name='bookmark'),
                  path('blog/', include('blog.urls'), name='blog'),
                  path('photo/', include('photo.urls'), name='photo'),
                  path('', HomeView.as_view(), name='home')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
