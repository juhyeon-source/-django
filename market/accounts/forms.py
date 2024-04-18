from django import forms
from accounts.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()