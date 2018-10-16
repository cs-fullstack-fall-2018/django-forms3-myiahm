from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('add/', views.add, name='add')
]