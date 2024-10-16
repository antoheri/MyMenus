from django.urls import path
from . import views

urlpatterns = [
    path("receipts/", views.ReceiptsList.as_view(), name="all-receipts"),
    path("receipt/", views.RandomReceipt.as_view(), name="random-receipt"),
    path("receipts/delete/<int:pk>/", views.ReceiptDelete.as_view(), name="delete-favorite"),
]
