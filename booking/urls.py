from django.urls import path
from . import views

urlpatterns = [
    path('add_train/', views.add_train, name='add_train'),
    path('view_trains/', views.view_trains, name='view_trains'),
    path('book_ticket/', views.book_ticket, name='book_ticket'),
]
