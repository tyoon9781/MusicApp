from django.urls import path
from app_music import views

app_name = "app_music"

urlpatterns = [
    path('', views.index, name="index"),
]