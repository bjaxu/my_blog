from django.shortcuts import render
from .models import VideoPost
from django.core.paginator import Paginator
# Create your views here.
# 视频列表
def video_list(request):
    video_list = VideoPost.objects.all()
    # 每页显示20篇文章
    paginator = Paginator(video_list,6)
    # 获取页码数
    page = request.GET.get('page')
    # 将页码数返回给books
    videos = paginator.get_page(page)
    context = {'videos':videos}
    return render(request, 'video/vlist.html', context)

# 视频详情
def video_detail(request, id):
    video = VideoPost.objects.get(id=id)
    context = {'video':video}
    return render(request, 'video/vdetail.html', context)
