from django.urls import path
from products import views

urlpatterns = [
    path('',views.home, name="home"),
    path('new/',views.new, name="new"),
]