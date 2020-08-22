from django.shortcuts import render, get_object_or_404

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
