from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost, ArticleColumn
import markdown
from .forms import ArticlePostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# 分页功能
from django.core.paginator import Paginator
# 搜索功能
from django.db.models import Q
from comment.models import Comment
# Create your views here.

# 首页列表
def article(request):
    # 拿到top10文章
    article_lists = ArticlePost.objects.all().order_by('-total_views')[0:10]
    # 拿到最新发布的 文章3篇
    articles = ArticlePost.objects.all()
    # 所有的栏目
    column = ArticleColumn.objects.all()
    context = {'articles':articles, 'article_lists':article_lists, 'columns':column}
    return render(request, 'base1.html', context)

# 文章列表
def article_list(request):
    # 拿到top10文章
    article_lists = ArticlePost.objects.all().order_by('-total_views')[0:10]
    article_list = ArticlePost.objects.all()
    # 每页显示10篇文章
    paginator = Paginator(article_list,10)
    # 获取页码数
    page = request.GET.get('page')
    # 将页码数返回给articles
    articles = paginator.get_page(page)
    # 所有的栏目
    column = ArticleColumn.objects.all()
    context = {'articles':articles, 'columns':column, 'article_lists':article_lists}
    return render(request, 'artilce/list.html', context)

# 文章详情
def artilce_detail(request, id):
    # 拿到top10文章
    article_lists = ArticlePost.objects.all().order_by('-total_views')[0:10]
    # 所有的栏目
    column = ArticleColumn.objects.all()
    article = ArticlePost.objects.get(id=id)
    # 取出评论文章
    comments = Comment.objects.filter(article=id)
    # 浏览量+1
    article.total_views += 1
    article.save(update_fields=['total_views'])
    # 将markdown语法 渲染成html样式
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ]
                                     )
    context = {'article':article,  'article_lists':article_lists, 'comments':comments, 'columns':column}
    return render(request, 'artilce/detail.html', context)

# 创建文章的视图
login_required(login_url='/userprofile/login/')
def article_create(request, mark_fu):
    if request.method == "POST":
        article_post_form = ArticlePostForm(request.POST, request.FILES )
        # 判断数据是否满足模型
        print(article_post_form)
        if article_post_form.is_valid():
            # 保存但不提交到数据库
            new_article = article_post_form.save(commit=False)
            # 作者
            new_article.author = User.objects.get(id=request.user.id)
            if request.POST['column'] != 'none':
                new_article.column = ArticleColumn.objects.get(id=request.POST['column'])
            new_article.save()
            return redirect('article:article_list')
        else:
            return HttpResponse('输入有误，请重新输入!')
    else:
        # 拿到top10文章
        article_lists = ArticlePost.objects.all().order_by('-total_views')[0:10]
        # 拿到所有标签
        column = ArticleColumn.objects.all()
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form, 'article_lists':article_lists, 'columns':column}
        if mark_fu == 1:
            return render(request, 'artilce/create1.html', context)
        elif mark_fu == 2:
            return render(request, 'artilce/create.html', context)


# 删除文章
login_required(login_url='/userprofile/login/')
def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.user != article.author:
        return HttpResponse('对不起，你没有修改权限!')
    article.delete()
    return redirect('article:article_list')

# 更新文章
login_required(login_url='/userprofile/login/')
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    # 过滤非作者
    if request.user != article.author:
        return HttpResponse('对不起，你没有修改权限!')
    if request.method == "POST":
        article.title = request.POST['title']
        article.body = request.POST['body']
        # 如果提交里面有标签
        if request.POST['column'] != 'none':
            article.column = ArticleColumn.objects.get(id=request.POST['column'])
        else:
            article.column = None
        article.save()
        return redirect('arctile:article_detail', id=id)
    else:
        # 拿到top10文章
        article_lists = ArticlePost.objects.all().order_by('-total_views')[0:10]
        columns = ArticleColumn.objects.all()
        column_now = ArticleColumn.objects.filter(id=article.column_id)
        if column_now:
            column_now = column_now[0].title
        else:
            column_now = ''
        article_post_form = ArticlePostForm()
        context = {'article':article ,
                   'article_post_form':article_post_form,
                   'article_lists':article_lists,
                   'columns':columns,
                   'column_now':column_now,
                   }
        return render(request, 'artilce/update1.html', context)

# 富文本更新文章
login_required(login_url='/userprofile/login/')
def article_update1(request, id):
    article = ArticlePost.objects.get(id=id)
    # 过滤非作者
    if request.user != article.author:
        return HttpResponse('对不起，你没有修改权限!')
    if request.method == "POST":
        article.title = request.POST['title']
        article.body1 = request.POST['body1']
        # 如果提交里面有标签
        if request.POST['column'] != 'none':
            article.column = ArticleColumn.objects.get(id=request.POST['column'])
        else:
            article.column = None
        article.save()
        return redirect('arctile:article_detail', id=id)
    else:
        # 拿到top10文章
        article_lists = ArticlePost.objects.all().order_by('-total_views')[0:10]
        columns = ArticleColumn.objects.all()
        column_now = ArticleColumn.objects.filter(id=article.column_id)
        if column_now:
            column_now = column_now[0].title
        else:
            column_now = ''
        article_post_form = ArticlePostForm()
        context = {'article':article ,
                   'article_post_form':article_post_form,
                   'article_lists':article_lists,
                   'columns':columns,
                   'column_now':column_now,
                   }
        return render(request, 'artilce/update.html', context)