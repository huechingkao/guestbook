from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessageListView.as_view()),
    path('message/<int:pk>', views.MessageDetailView.as_view()),
    path('message/create/', views.MessageCreate.as_view()),  
    path('message/<int:pk>/delete/', views.MessageDelete.as_view()),   
]