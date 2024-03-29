from rest_framework import viewsets, generics
from .models import product, message, bag, product, ProductNote
from .serializers import productSerializer, productDetailSerializer, messageSerializer, bagSerializer, sacoleiraProductsSerializer, searchSacoleirasSerializer, productNoteSerializer
from rest_framework import permissions, authentication, filters
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser


class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]


class productNoteViewSet(viewsets.ModelViewSet):
    queryset = ProductNote.objects.all()
    serializer_class = productNoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    

class messageViewSet(viewsets.ModelViewSet):
    queryset = message.objects.all()
    serializer_class = messageSerializer
    

class bagViewSet(viewsets.ModelViewSet):
    serializer_class = bagSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    
    def get_queryset(self):
        user = self.request.user
        return bag.objects.filter(user=user)


class sacoleiraProducts(generics.ListAPIView):
    serializer_class = sacoleiraProductsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'size']
    
    def get_queryset(self):
        return product.objects.filter(sacoleira_id=self.kwargs["id"])


class productDetail(generics.RetrieveAPIView):
    serializer_class = productDetailSerializer
    
    def get_queryset(self):
        return product.objects.filter(id=self.kwargs['pk'])
