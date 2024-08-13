from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_todo, name='add-todo'),
    path('delete/<int:id>', views.delete, name='delete-todo'),
    path('edit/<int:id>', views.edit, name='edit-todo')

]