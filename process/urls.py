from django.urls import path

from . import views

urlpatterns=[
    path('', views.processes_list, name='processes_list'),
    path('<int:pk>/', views.processes_detail, name='processes_detail'),
    path('<int:pk>/delete/', views.processes_delete, name='processes_delete'),
    path('<int:pk>/edit/', views.processes_edit, name='processes_edit'),
    path('add-process/', views.add_process, name='add_process'),

]