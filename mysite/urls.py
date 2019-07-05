from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite import settings
from mysite.views import HomeView, UserCreateDoneTV, UserCreateTV

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateTV.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    path('bookmark/', include('bookmark.urls'), name='bookmark'),
    path('blog/', include('blog.urls'), name='blog'),
    path('photo/', include('photo.urls'), name='photo'),
    path('', HomeView.as_view(), name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
