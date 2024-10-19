from django.shortcuts import render
from .models import Order
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()
        status = order.get_order_status()
        serializer = self.get_serializer(order)

        return Response({
            'order': serializer.data,
            'order_status': status
        })
    
    def perform_destroy(self, instance):
        instance.delete()

# Create your views here.
