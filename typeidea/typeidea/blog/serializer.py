from rest_framework import serializers,pagination
from django.contrib.auth.models import User
from .models import Post,Category,Tag

class PostSerializer(serializers.HyperlinkedModelSerializer):
    category=serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    tag=serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    owner=serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    created_time=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    url=serializers.HyperlinkedIdentityField(view_name='api-post-detail')

    class Meta:
        model=Post
        fields=['url','id','title','category','tag','owner','created_time']

class PostDetailSerializer(PostSerializer):
    class Meta:
        model=Post
        fields=['id','title','category','tag','owner','content_html','created_time']

class CategorySerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='api-category-detail')
    class Meta:
        model=Category
        fields=(
            'url','id','name','created_time',
        )

class CategoryDetailSerializer(CategorySerializer):
    posts=serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self,obj):
        posts=obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator=pagination.PageNumberPagination()
        page=paginator.paginate_queryset(posts,self.context['request'])
        serializer=PostSerializer(page,many=True,context={'request':self.context['request']})
        return {
            'count':posts.count(),
            'results':serializer.data,
            'previous':paginator.get_previous_link(),
            'next':paginator.get_next_link(),
        }
    class Meta:
        model=Tag
        fields=(
            'id','name','created_time','posts'
        )

class TagSerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='api-tag-detail')
    class Meta:
        model=Tag
        fields=(
            'url','id','name','created_time',
        )

class TagDetailSerializer(TagSerializer):
    posts=serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self,obj):
        posts=obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator=pagination.PageNumberPagination()
        page=paginator.paginate_queryset(posts,self.context['request'])
        serializer=PostSerializer(page,many=True,context={'request':self.context['request']})
        return {
            'count':posts.count(),
            'results':serializer.data,
            'previous':paginator.get_previous_link(),
            'next':paginator.get_next_link(),
        }
    class Meta:
        model=Tag
        fields=(
            'id','name','created_time','posts'
        )

class UserSerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='api-author-detail')
    class Meta:
        model=User
        fields=(
            'url','id','username',
        )

class UserDetailSerializer(TagSerializer):
    posts=serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self,obj):
        posts=obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator=pagination.PageNumberPagination()
        page=paginator.paginate_queryset(posts,self.context['request'])
        serializer=PostSerializer(page,many=True,context={'request':self.context['request']})
        return {
            'count':posts.count(),
            'results':serializer.data,
            'previous':paginator.get_previous_link(),
            'next':paginator.get_next_link(),
        }
    class Meta:
        model=User
        fields=(
            'id','username','posts'
        )