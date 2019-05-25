from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

# 每篇文章的栏目
class ArticleColumn(models.Model):
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# 博客文章数据模型
class ArticlePost(models.Model):
    # 标题
    title = models.CharField(max_length=100)
    # 作者 一个用户对应着多个文章，级联删除
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章正文 Markdown
    body = models.TextField(blank=True)
    # 文章正文 富文本模式编写
    body1 = RichTextUploadingField(blank=True)
    # 创建时间 默认写入创建时的时间
    created_time = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated_time = models.DateTimeField(auto_now=True)
    # 浏览量
    total_views = models.PositiveIntegerField(default=0)
    # 文章栏目
    column = models.ForeignKey(ArticleColumn, null=True,blank=True, on_delete=models.CASCADE, related_name='article')
    # 文章图片
    avatar = ProcessedImageField(
        upload_to='article/%Y%m%d',
        processors=[ResizeToFill(220,150)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
    )

    class Meta:
        # 数据排序方式 倒序方式排序
        ordering = ('-created_time',)

        # 将文章标题返回
        def __str__(self):
            return self.title

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])



