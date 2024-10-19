from django.urls import path
from .views import ProductListCreateView, ProductdetailView, ProductSearchView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductdetailView.as_view(), name='product-detail'),
    path('search/', ProductSearchView.as_view(), name='product-search'),
]