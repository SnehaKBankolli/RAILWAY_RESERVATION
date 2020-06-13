from django.urls import path,include
from .import views

urlpatterns = [
   
    path('',views.index),
    path('details/<str:pk>/',views.details,name="details"),
    path('book/<str:pk>/',views.book_ticket,name="book_ticket"),
    path('view_tickets/<str:pk>',views.view_tickets,name="view_tickets"),
    
]