from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Comment
from .serializer import CommentSerializer,CommentDetailSerializer

class CommentViewSet(viewsets.ModelViewSet):
    
    serializer_class=CommentSerializer
    queryset=Comment.objects.filter(status=Comment.STATUS_NORMAL)
    #permission_classes=[IsAdminUser]

    def retrieve(self,request,*args,**kwargs):
        self.serializer_class=CommentDetailSerializer
        return super().retrieve(request,*args,**kwargs)