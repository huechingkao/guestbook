from django.shortcuts import render
from django.views import generic
from django import forms
from .models import Message
from .forms import MessageForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class MessageListView(generic.ListView):
    model = Message
    ordering = ['-id']    
    
class MessageDetailView(generic.DetailView):
    model = Message
    
class MessageCreate(CreateView):
    # model = Message
    # fields = ['user', 'subject', 'content']
    form_class = MessageForm
    success_url = "/"   
    template_name = 'form.html'      
    
class MessageDelete(DeleteView):
    model = Message
    success_url = "/"
    template_name = 'confirm_delete.html'      