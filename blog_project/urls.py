from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('category/<slug:category_slug>/', views.home, name="category_filter"),
    path('authors/', include('authors.urls')),
    path('categories/', include('categories.urls')),
    path('posts/', include('posts.urls')),
]

# media files will be working in both debug=True and debug=False. that means both in development and production.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# settings.MEDIA_URL is Base url to serve media files.
# document_root = settings.MEDIA_ROOT is used to tell django where to look for the media files (this line is for global media files otherwise if its inside the app then no needed cause already whole app is defined in installed app).
