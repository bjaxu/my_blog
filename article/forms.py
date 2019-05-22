# 引入表单类
from django import forms
from .models import ArticlePost

class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 数据来源
        model = ArticlePost
        fields = {'title', 'body', 'avatar', 'body1'}
