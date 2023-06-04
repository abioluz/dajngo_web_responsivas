from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('',views.home, name='home'),
    path('blog',views.blog, name='blog'),
    path('posts/<int:post_id>/',views.post_detail, name='post_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)