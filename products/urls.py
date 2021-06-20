from django.urls import path
from products import views

urlpatterns = [
    path('',views.home, name="home"),
    path('new/',views.new, name="new"),
    path('archivos/', views.cargar_archivo, name="archivos"),
    path('mod/<p_id>/', views.mod, name="mod"),
]