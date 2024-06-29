from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('completed/<int:id>', views.completed, name='completed'),
    path('task1', views.task1, name='task1'),
    path('edit/<int:id>', views.edit, name='edit'),
   path('update/<int:id>', views.update, name='update')
]
