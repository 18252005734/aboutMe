# Create your views here.
#coding:utf-8
from WebManage.models import Column, Article
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
 
    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
    })

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'WebManage/column.html', {'column': column})
 
 
def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
 
    if article_slug != article.slug:
        return redirect(article, permanent=True)
 
    return render(request, 'WebManage/article.html', {'article': article})
