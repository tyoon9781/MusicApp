from django.urls import path
from app_account import views

app_name = "app_account"

urlpatterns = [
    path('', views.index, name="index"),
]