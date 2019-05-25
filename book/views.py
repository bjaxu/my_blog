from django.shortcuts import render, redirect
from  .models import BookPost
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from qiniu import Auth
import requests

access_key = 'lWGrdnCe4PYfR1oXKAJHtAPikJ0bKGl-XqksUl0z'
secret_key = 'YzAEvTs_p8RVNcbPtgVMPnpFmm1QnbNc0HaxaXTx'
q = Auth(access_key, secret_key)

# Create your views here.
# 书籍列表
def book_list(request):
    book_list = BookPost.objects.all()
    # 每页显示20篇文章
    paginator = Paginator(book_list,20)
    # 获取页码数
    page = request.GET.get('page')
    # 将页码数返回给books
    books = paginator.get_page(page)
    context = {'books':books}
    return render(request, 'book/blist.html', context)

#书籍详情
def book_detail(request, id):
    book = BookPost.objects.get(id=id)
    context = {'book':book}
    return render(request, 'book/bdetail.html', context)

# 书籍下载
def download(request, id):
    book = BookPost.objects.filter(id=id)
    filename = book[0].downname
    # 或者直接输入url的方式下载
    base_url = 'http://prucutqgp.bkt.clouddn.com/' + filename
    # 可以设置token过期时间
    private_url = q.private_download_url(base_url, expires=3600)
    return redirect(private_url)