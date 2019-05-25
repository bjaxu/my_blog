from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from .forms import ProfileForm
from .models import Profile

# Create your views here.
# 用户登录
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        next = request.POST.get('next', 'article:article_list')
        if user_login_form.is_valid():
            # 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检查账号密码是否匹配数据库中的某个用户，如果满足则返回这个user对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                print(next)
                return HttpResponse(json.dumps({'statue':1, 'next':next}))
            else:
                return HttpResponse(json.dumps({'statue':0, 'next':''}))
    return HttpResponse(json.dumps({'statue': 0, 'next': ''}))

# 用户退出
def user_logout(request):
    logout(request)
    return redirect('article:article')

#用户注册
def user_register(request):
    if request.method == "POST":
        invite_code = request.POST.get('invite', '')
        if invite_code == '123456':
            user_register_form = UserRegisterForm(data=request.POST)
            if user_register_form.is_valid():
                data = user_register_form.cleaned_data
                email = User.objects.filter(email=data['email'])
                # 3表示邮箱存在
                if email:
                    return render(request, 'userprofile/register.html', {'statue': 3})

                else:
                    new_user = user_register_form.save(commit=False)
                    # 设置密码
                    new_user.set_password(user_register_form.cleaned_data['password'])
                    new_user.save()
                    #登录
                    login(request, new_user)
                    # 4表示注册成功
                    return render(request, 'userprofile/register.html', {'statue': 4})
            else:
                # 2表示用户名已经存在
                error = user_register_form.errors
                return render(request, 'userprofile/register.html', {'statue': 2})
        else:
            # 1是注册码错误
            return render(request, 'userprofile/register.html',{'statue': 1})
    elif request.method == "GET":
        user_register_form = UserRegisterForm()
        context = {'form':user_register_form}
        return render(request, 'userprofile/register.html', context)
    else:
        return ('用户注册发生错误!')

# 用户协议
def user_agree(request):
    if request.method == "GET":
        return render(request, 'userprofile/agreement.html')

# 用户删除
@login_required(login_url='/useprofile/login/')
def user_delete(request, id):
    user = User.objects.get(id=id)
    # 验证登录用户和待删除用户是否相同
    if request.user == user:
        logout(request)
        user.delete()
        return redirect('article:article_list')
    else:
        return HttpResponse('你没有删除的权利！')

# 修改个人资料
@login_required(login_url='/useprofile/login/')
def profile_edit(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=id)
    if request.method == "POST":
        if request.user != user:
            return HttpResponse("你没有权限修改此用户信息。")
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            # 取得清洗后的合法数据
            profile_cd = profile_form.cleaned_data
            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']
            if 'avatar' in request.FILES:
                profile.avatar = profile_cd['avatar']
            profile.save()
            # 带参数的 redirect()
            return redirect("userprofile:edit", id=id)
        else:
            return HttpResponse("注册表单输入有误。请重新输入!")
    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = {'profile_form':profile_form, 'profile':profile, 'user':user}
        return render(request, 'userprofile/edit.html', context)
    else:
        return HttpResponse('使用get或者post请求!')