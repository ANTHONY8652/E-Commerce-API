from django.shortcuts import render
from .models import Product, Category
from .serializers import ProductSerializer
from rest_framework import generics, permissions, filters

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        category_name = self.request.data.get('category')
        category, _ = Category.objects.get_or_create(name=category_name)
        serializer.save(category=category, owner=self.request.user)

class ProductdetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name']

    def get_queryset(self):
        return Product.objects.all()


# Create your views here.
