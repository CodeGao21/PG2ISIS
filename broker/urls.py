from django.urls import path

from . import views

urlpatterns = [
    path('',views.brokers_list, name='brokers_list'),
    path('<int:pk>/', views.brokers_detail, name='brokers_detail'),
    path('<int:pk>/delete/', views.brokers_delete, name='brokers_delete'),
    path('<int:pk>/edit/', views.brokers_edit, name='brokers_edit'),
    path('add-broker/', views.add_broker, name='add_broker'),
]