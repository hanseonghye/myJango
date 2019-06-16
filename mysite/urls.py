from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
	path('bookmark/', include('bookmark.urls'), name='bookmark'),
	path('blog/', include('blog.urls'), name='blog'),
	path('',HomeView.as_view(),name ='home')
]
