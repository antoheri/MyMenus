from django.shortcuts import render
from django.db.models.functions import Random
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ReceiptSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Receipt

# Display the list of all receipts
class ReceiptsList(generics.ListCreateAPIView):
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]
    queryset = Receipt.objects.all()

# Display the details of a randomly selected receipt
class RandomReceipt(generics.ListAPIView):
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Receipt.objects.order_by(Random())[:1]

# Display the list of all receipts created by the user (not implemented)
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

class CreateReceiptView(generics.CreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]
