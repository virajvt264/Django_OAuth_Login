from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  # Home page
    path('logout/', views.logout_view, name='logout'),  # Logout view
]