from django import forms
from accounts.models import Article
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )