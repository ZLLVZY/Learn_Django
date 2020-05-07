from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User

from .models import Post,Category,Tag
from .serializer import (
    PostSerializer,PostDetailSerializer,
    CategorySerializer,CategoryDetailSerializer,
    TagSerializer,TagDetailSerializer,
    UserSerializer,UserDetailSerializer,
)

class PostViewSet(viewsets.ModelViewSet):
    
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=Post.STATUS_NORMAL)
    #permission_classes=[IsAdminUser]

    def retrieve(self,request,*args,**kwargs):
        self.serializer_class=PostDetailSerializer
        return super().retrieve(request,*args,**kwargs)

    def filter_queryset(self,queryset):
        category_id=self.request.query_params.get('category')
        if category_id:
            queryset=queryset.filter(category_id=category_id)
        return queryset

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class=CategorySerializer
    queryset=Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self,request,*args,**kwargs):
        self.serializer_class=CategoryDetailSerializer
        return super().retrieve(request,*args,**kwargs)

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class=TagSerializer
    queryset=Tag.objects.filter(status=Tag.STATUS_NORMAL)

    def retrieve(self,request,*args,**kwargs):
        self.serializer_class=TagDetailSerializer
        return super().retrieve(request,*args,**kwargs)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    def retrieve(self,request,*args,**kwargs):
        self.serializer_class=UserDetailSerializer
        return super().retrieve(request,*args,**kwargs)