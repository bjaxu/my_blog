from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class VideoPost(models.Model):
    # 标题
    title = models.CharField(max_length=100)
    # 作者 一个用户对应着多个文章，级联删除
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 创建时间 默认写入创建时的时间
    created_time = models.DateTimeField(default=timezone.now)
    # 图片地址
    image_url = models.CharField(max_length=100)
    # 视频地址
    video_url =  models.CharField(max_length=100, blank=True)

    class Meta:
        # 数据排序方式 倒序方式排序
        ordering = ('-created_time',)

        # 将文章标题返回
        def __str__(self):
            return self.title