from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """view main home page"""
    # return HttpResponse("참새공주와 탑건 영화 데이트")
    return render(request, "app_music/index.html")
    