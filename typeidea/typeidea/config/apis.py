from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Link,SideBar
from .serializer import LinkSerializer,LinkDetailSerializer,SideBarSerializer,SideBarDetailSerializer

class LinkViewSet(viewsets.ModelViewSet):
    
    serializer_class=LinkSerializer
    queryset=Link.objects.filter(status=Link.STATUS_NORMAL)
    #permission_classes=[IsAdminUser]

    def retrieve(self,request,*args,**kwargs):
        self.serializer_class=LinkDetailSerializer
        return super().retrieve(request,*args,**kwargs)

class SideBarViewSet(viewsets.ModelViewSet):
    
    serializer_class=SideBarSerializer
    queryset=SideBar.objects.filter(status=SideBar.STATUS_SHOW)
    #permission_classes=[IsAdminUser]

    def retrieve(self,request,*args,**kwargs):
        self.serializer_class=SideBarDetailSerializer
        return super().retrieve(request,*args,**kwargs)