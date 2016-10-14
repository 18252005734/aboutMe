"""aboutMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'WebManage.views.index', name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', 'WebManage.views.column_detail', name='column'),
    #url(r'^WebManage/(?P<article_slug>[^/]+)/$', 'WebManage.views.article_detail', name='article'),
    url(r'^WebManage/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', 'WebManage.views.article_detail', name='article'),    

    url(r'^ueditor/', include(DjangoUeditor_urls)),
]

urlpatterns += staticfiles_urlpatterns()
from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
