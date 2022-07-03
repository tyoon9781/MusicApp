from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """view main home page"""
    return HttpResponse("render account page")
    