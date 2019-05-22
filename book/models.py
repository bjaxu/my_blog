from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# 书籍的数据模型
class BookPost(models.Model):
    # 标题
    title = models.CharField(max_length=100)
    # 作者
    author = models.CharField(max_length=100)
    # 创建时间 默认写入创建时的时间
    created_time = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated_time = models.DateTimeField(auto_now=True)
    # 下载文件名
    downname = models.CharField(max_length=100, blank=True)
    # 文章简介
    body = models.TextField(blank=True)
    # 文章正文 富文本模式编写
    body1 = RichTextUploadingField(blank=True)
    # 文章图片
    avatar = ProcessedImageField(
        upload_to='book/%Y%m%d',
        processors=[ResizeToFill(128,170)],
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
