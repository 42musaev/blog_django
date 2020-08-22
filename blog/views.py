from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from blog.forms import AddArticleForm
from blog.models import Article


def home(request):
    try:
        last_article = Article.objects.filter().order_by('-date_pub')[0]
    except:
        last_article = []
    articles = Article.objects.filter().order_by('-date_pub')[:10]
    return render(request, 'blog/index.html', {
        'articles': articles,
        'last_article': last_article,
    })


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', {'article': article})


class ArticleAdd(View):
    def get(self, request):
        form = AddArticleForm()
        return render(request, 'blog/article_add.html', {'form': form})

    def post(self, request):
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save()
            return redirect(new_article)
        return render(request, 'blog/article_add.html', {'form': form})
