from django.urls import path
from . import views
app_name = 'video'

urlpatterns = [
    # 视频列表
    path('video-list/', views.video_list, name='video_list'),
    # 视频详情
    path('video-detail/<int:id>/', views.video_detail, name='video_detail'),
]