# machines_services/urls.py
from django.urls import path
from machines import views

urlpatterns = [
    path('machines/', views.MachineListCreate.as_view(), name='machine-list-create'),
    path('machines/<int:pk>/', views.MachineRetrieveUpdateDestroy.as_view(), name='machine-detail'),
]
