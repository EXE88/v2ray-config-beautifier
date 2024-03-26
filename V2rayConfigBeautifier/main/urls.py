from django.urls import path
from . import views

urlpatterns = [
   path('' , views.InputCodePageView.as_view()), 
]
