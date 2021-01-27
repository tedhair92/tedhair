from django.urls import path, include
from . import views

# app_name = "tedhair"

urlpatterns = [
    path('', views.index, name="home"),
    path('tedhair/', views.frmUserDetails, name="userinput"),
]
