# payments/urls.py

from django.urls import path
from .views import PaymentListCreate, PaymentRetrieveUpdateDestroy

urlpatterns = [
    path('payments/', PaymentListCreate.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroy.as_view(), name='payment-retrieve-update-destroy'),
]
