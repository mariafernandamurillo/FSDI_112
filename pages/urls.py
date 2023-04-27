from django.urls import path
#from this folder (.) import this class (HomePageView)
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]