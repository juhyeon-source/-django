from django.shortcuts import render
from .models import Article

def product_list(request):
    articles = Article.objects.all()
    context = {"articles" : articles,}
    return render(request, 'product_list.html', context)
