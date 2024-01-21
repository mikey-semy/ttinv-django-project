from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalogs/<slug:catalog_slug>/", views.catalogs, name="catalogs"),
    
]
