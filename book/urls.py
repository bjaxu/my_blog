from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    # 书籍列表
    path('book-list/', views.book_list, name='book_list'),
    # 书籍详情
    path('book-detail/<int:id>/', views.book_detail, name='book_detail'),
    # 书籍下载
    path('book-download/<int:id>/', views.download, name='download'),
]