from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    # 图片列表
    path('photo-list/', views.photo_list, name='photo_list'),
]