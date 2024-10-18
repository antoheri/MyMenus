from django.urls import path
from . import views

urlpatterns = [
    path("receipts/", views.ReceiptsList.as_view(), name="all-receipts"),
    path("receipt/", views.RandomReceipt.as_view(), name="random-receipt"),
    path("receipt/create", views.CreateReceiptView.as_view(), name="create-receipt"),
    path("receipts/delete/<int:pk>/", views.ReceiptDelete.as_view(), name="delete-favorite"),
    path("favourites/", views.ListFavouriteView.as_view(), name="favourites"),
]
