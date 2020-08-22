from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = 'index' ),
    path('home/<int:pk>', views.homeDetails, name = 'home-details' ),
    path('all-homes/',views.allHomes, name='all-homes'),
    path('agents/', views.agents, name='agents'),
    path('agent/<int:pk>/', views.individualAgent, name='individual-agent'),
    path('register/', views.registerUser, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('dashboard/<int:pk>/', views.dashboard, name = 'dashboard'),


]