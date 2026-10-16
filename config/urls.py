from django.urls import path

from portfolio.views import health, home


urlpatterns = [
    path("", home, name="home"),
    path("health/", health, name="health"),
]
