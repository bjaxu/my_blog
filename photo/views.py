from django.shortcuts import render
from .models import PhotoPost
# Create your views here.

# 照片列表
def photo_list(request):
    photo_list = PhotoPost.objects.all()
    context = {'photo_lists': photo_list}
    return render(request, 'photo/plist.html', context)
