from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("about/", views.about, name="about"),
    path('collection/<int:n>/', views.collection_detail, name='collection_detail'),
    path("all/", views.index, name="index"),
    path('new/', views.new_collec, name='new_collec'),
    path('delete/<int:collec_id>', views.delete_collec, name="delete_collec"),
    path("change/<int:collec_id>", views.edit_collec, name="edit_collec"),


    path('element/add/', views.ajout_element, name='ajout_element'),
    path('element/delete/<int:element_id>', views.delete_element, name="delete_element"),
    path('element/<int:n>/', views.element_detail, name='element_detail'),
    path("element/edit/<int:element_id>", views.edit_element, name="edit_element"),

    
  
]