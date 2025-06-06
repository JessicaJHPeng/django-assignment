from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name="home"),
    path('all/', views.all, name="All Entries"),
    path('search/', views.search, name="Search"),
    path('import/', views.import_data, name="Import JSON")
]
