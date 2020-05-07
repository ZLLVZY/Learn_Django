from rest_framework import serializers,pagination
from django.contrib.auth.models import User
from .models import Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='api-comment-detail')
    class Meta:
        model=Comment
        fields=['url','id','target','nickname']

class CommentDetailSerializer(CommentSerializer):
    class Meta:
        model=Comment
        fields=['id','target','nickname','content']