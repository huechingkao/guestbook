from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessageListView.as_view()),
    path('create/', views.MessageCreate.as_view()),  
    path('<int:pk>', views.MessageDetailView.as_view()),
    path('<int:pk>/delete/', views.MessageDelete.as_view()),   
]