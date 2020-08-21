from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = 'index' ),
    path('home/<int:pk>', views.homeDetails, name = 'home-details' ),

]