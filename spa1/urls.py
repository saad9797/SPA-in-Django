from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.sections , name="section"),
    path("scroll", views.Scroll, name="Scroll")
]