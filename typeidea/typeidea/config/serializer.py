from rest_framework import serializers,pagination
from .models import Link,SideBar

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    owner=serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    url=serializers.HyperlinkedIdentityField(view_name='api-link-detail')
    class Meta:
        model=Link
        fields=['url','title','owner','created_time']

class LinkDetailSerializer(LinkSerializer):
    class Meta:
        model=Link
        fields=['title','href','owner','weight','created_time']

class SideBarSerializer(serializers.HyperlinkedModelSerializer):
    owner=serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    url=serializers.HyperlinkedIdentityField(view_name='api-sidebar-detail')
    class Meta:
        model=SideBar
        fields=['url','title','owner','display_type','created_time']

class SideBarDetailSerializer(SideBarSerializer):
    class Meta:
        model=SideBar
        fields=['title','owner','display_type','content','created_time']