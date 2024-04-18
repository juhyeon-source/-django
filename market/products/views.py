from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def product_list(request):
    articles = Article.objects.all().order_by('-id')
    context = {"articles" : articles,}
    return render(request, 'products/product_list.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("products:product_detail", article.id)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "products/create.html", context)

def product_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article" : article}
    return render(request, 'products/product_detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('products:product_list')
    return redirect('products:product_detail', article.pk)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("products:product_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "products/update.html", context)




