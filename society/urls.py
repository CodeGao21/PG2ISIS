from django.urls import path

from . import views

urlpatterns = [
    path('',views.societies_list, name='societies_list'),
    path('<int:pk>/', views.societies_detail, name='societies_detail'),
    path('<int:pk>/propertyprocess/', views.propierties_process_detail, name='propierties_process_detail'),
    path('<int:pk>/delete/', views.societies_delete, name='societies_delete'),
    path('<int:pk>/edit/', views.societies_edit, name='societies_edit'),
    path('add-society/', views.add_society, name='add_society'),
]