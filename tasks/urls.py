from django.urls import path
from . import views

urlpatterns =[

path('', views.index ,name="list"),
path('Update_task/<str:pk>/', views.Updatetask, name="update_task"),
path('delete/<str:pk>/', views.deleteTask, name="delete"),

]
