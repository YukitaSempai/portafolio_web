from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def health(request):
    return HttpResponse("ok", content_type="text/plain")
