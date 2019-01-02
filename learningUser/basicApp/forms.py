from django import forms
from django.contrib.auth.models import User
from basicApp.models import UserInfoModel

class UserInfo(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserInfoModelForm(forms.ModelForm):
    class Meta():
        model = UserInfoModel
        fields = ('portfolio_site','portfolio_image')
