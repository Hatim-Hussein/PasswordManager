from django.urls import path
from . import views
from .views import  AutoFillAll, AutoFill

urlpatterns = [
    path('', views.home, name="home"),
    path('api/auto/all', AutoFillAll.as_view(), name="autofillall"),
    path('api/auto', AutoFill.as_view(), name="autofill"),
    
]