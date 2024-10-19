from django.urls import path
from .views import OrderDetailView, OrderListCreateView

urlpattersn = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]