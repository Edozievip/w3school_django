from django.urls import path

from . import views


urlpatterns = [
    path("index/", views.index, name="index"),
    path('index/details/<int:id>', views.details, name="details"),
    path("", views.home, name="home"),
    path("testing/", views.testing, name="testing")
]
