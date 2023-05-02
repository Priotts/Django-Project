from django.urls import path
from . import views

urlpatterns = [
    path('', views.w3school, name='w3school'),
    path('admin_log', views.admin_log, name='admin_log'),
    path('logout/', views.logout_view, name = 'logout'),
]