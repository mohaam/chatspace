from django.urls import path

from . import views

urlpatterns = [
    path('chat/<room_name>/', views.chatroom, name='chatroom'),
    path('logout', views.log, name='logout')
]