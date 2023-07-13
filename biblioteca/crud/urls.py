from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path('base/', views.base, name="base"),
    path('view_libro/<int:id>/', views.view_libro, name='view_libro'),
    path('add/', views.add, name='add'),
    path('compras/', views.compras, name='compras'),
    path('edit/<int:id>/', views.edita, name='edit'),
    path('eliminar/<int:id>/', views.elimina, name="eliminar"),
    path('login/',LoginView.as_view(template_name='crud/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='crud/logout.html'), name='logout'),
    path('registrar/',views.registrar ,name='register'),
]
