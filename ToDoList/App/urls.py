from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
    path('delete/<int:id>', views.delete.as_view(), name="delete"),
    path('edit/<int:id>', views.editTask.as_view(), name="edit"),
]