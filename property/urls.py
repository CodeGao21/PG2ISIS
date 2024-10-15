from django.urls import path

from . import views

urlpatterns=[
    path('', views.properties_list, name='properties_list'),
    path('<int:pk>/', views.properties_detail, name='properties_detail'),
    path('<int:pk>/delete/', views.properties_delete, name='properties_delete'),
    path('<int:pk>/edit/', views.properties_edit, name='properties_edit'),
    path('add-property/', views.add_property, name='add_property'),

]