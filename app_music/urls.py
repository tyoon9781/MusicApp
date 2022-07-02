from django.urls import URLPattern, path
from app_music import views


urlpatterns = [
    path('', views.index, name="index"),
]