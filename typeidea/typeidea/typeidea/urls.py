"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .custom_site import custom_site
from django.contrib.sitemaps import views as sitemap_views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from typeidea.settings import develop

#from blog.views import post_list,post_detail  function view
from blog.views import (
        IndexView,CategoryView,TagView,
        PostDetailView,
        SearchView,
        AuthorView,
        )

from config.views import LinkListView
from comment.views import CommentView
from blog.apis import PostViewSet,CategoryViewSet,TagViewSet,UserViewSet
from comment.apis import CommentViewSet
from config.apis import LinkViewSet,SideBarViewSet

router=DefaultRouter()
router.register('post',PostViewSet,basename='api-post')
router.register('category',CategoryViewSet,basename='api-category')
router.register('tag',TagViewSet,basename='api-tag')
router.register('author',UserViewSet,basename='api-author')
router.register('comment',CommentViewSet,basename='api-comment')
router.register('link',LinkViewSet,basename='api-link')
router.register('sidebar',SideBarViewSet,basename='api-sidebar')

urlpatterns = [
    #path('super_admin/', admin.site.urls,name='super-admin'),
    path('admin/',admin.site.urls,name='admin'),
    path('',IndexView.as_view(),name='index'),
    path('category/<int:category_id>/',CategoryView.as_view(),name='category-list'),
    path('tag/<int:tag_id>/',TagView.as_view(),name='tag-list'),
    path('post/<int:post_id>.html',PostDetailView.as_view(),name='post-detail'),
    path('search/',SearchView.as_view(),name='search'),
    path('author/<int:owner_id>',AuthorView.as_view(),name='author'),
    path('links',LinkListView.as_view(),name='links'),
    path('comment/',CommentView.as_view(),name='comment'),
    path('rss',LatestPostFeed(),name='rss'),
    path('sitemap.xml',sitemap_views.sitemap,{'sitemaps':{'posts':PostSitemap}}),
    path('api/',include(router.urls),name='api'),
    path('api/docs/',include_docs_urls(title='typeidea apis')),
]

if develop.DEBUG:
    import debug_toolbar
    urlpatterns=[
        path('__debug__',include(debug_toolbar.urls)),
    ]+urlpatterns
