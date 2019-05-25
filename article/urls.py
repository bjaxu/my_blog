from django.urls import path
from . import views
# 引入path
app_name = 'article'

urlpatterns = [
    # 首页
    path('article/',views.article, name='article'),
    # 文章列表
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情
    path('article-detail/<int:id>', views.artilce_detail, name='article_detail'),
    # 创建文章
    path('article-create/<int:mark_fu>', views.article_create, name='article_create'),
    # 删除文章
    path('article-delete/<int:id>', views.article_delete, name='article_delete'),
    # 修改文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    # 富文本修改文章
    path('article-update1/<int:id>/', views.article_update1, name='article_update1'),
]