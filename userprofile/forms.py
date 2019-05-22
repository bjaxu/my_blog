from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

# 注册用户表单
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = {'username', 'email'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') == cd.get('password2'):
            return cd.get('password')
        else:
            raise forms.ValidationError('密码输入不一致，请重新输入!')

# 个人资料表单
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'avatar', 'bio')