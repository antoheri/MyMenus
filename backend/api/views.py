from django.shortcuts import render
from django.db.models.functions import Random
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ReceiptSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Receipt


# Create your views here.
class ReceiptsList(generics.ListCreateAPIView):
    serializer_class = ReceiptSerializer
    permission_classes = [AllowAny]
    queryset = Receipt.objects.all()

class RandomReceipt(generics.ListAPIView):
    serializer_class = ReceiptSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Receipt.objects.order_by(Random())[:1]


class ReceiptFavouriteList(generics.ListCreateAPIView):
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Receipt.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
    
class ReceiptDelete(generics.DestroyAPIView):
    serializer_class = ReceiptSerializer
    permission_classes  =[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Receipt.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
