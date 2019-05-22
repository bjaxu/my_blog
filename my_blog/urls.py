"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 用户管理页面
    path('admin/', admin.site.urls),
    # 文章界面
    path('article/', include('article.urls', namespace='arctile')),
    # 用户管理界面
    path('profile/', include('userprofile.urls', namespace='userporfile')),
    # 密码重置
    path('password-reset/', include('password_reset.urls')),
    # 用户评论
    path('comment/', include("comment.urls", namespace='comment')),
    # 上传文件
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # 书籍
    path('book/', include('book.urls', namespace='book')),
    # 视频
    path('video/', include('video.urls', namespace='video')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)