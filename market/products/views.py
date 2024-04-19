from django.shortcuts import get_object_or_404, render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import get_user_model


def product_list(request):
    articles = Article.objects.all().order_by('-id')
    # member = get_object_or_404(get_user_model(), username=username)
    context = {
        "articles" : articles,
        # "member" : member,
    }
    return render(request, 'products/product_list.html', context)

@require_http_methods(["GET", "POST"])
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

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        article.delete()
        return redirect('products:product_list')
    return redirect('products:product_detail', article.pk)

@require_http_methods(["GET", "POST"])
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

@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
    else:
        return redirect("accounts:login")

    return redirect("products:product_list")


