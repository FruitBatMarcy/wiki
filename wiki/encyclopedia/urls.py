from django.urls import path

from . import views

app_name="wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("newentry", views.newentry, name="newentry"),
    path("<str:title>", views.entry, name="entry"),
    
]
