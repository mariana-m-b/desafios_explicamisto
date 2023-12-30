# urls.py
from django.urls import path
#from .views import HomeView

#urlpatterns = [
#    path("", HomeView.as_view(), name="home"),
#]

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("grades/", views.grades , name="grades"),
]
