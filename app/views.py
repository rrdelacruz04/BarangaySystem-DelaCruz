from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Resident



    
    

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ResidentListView(ListView):
    model = Resident
    context_object_name = 'resident'
    template_name = 'app/resident_list.html'

class ResidentDetailView(DetailView):
    model = Resident
    context_object_name = 'resident'
    template_name = 'app/resident_detail.html'

class ResidentCreateView(CreateView):
    model = Resident
    fields = ['user', 'full_name', 'username', 'address', 'contact_number', 'email', 'status']
    template_name = 'app/resident_create.html'

class ResidentUpdateView(UpdateView):
    model = Resident
    fields = ['user','full_name', 'username', 'address', 'contact_number', 'email', 'status']
    template_name = 'app/resident_update.html'
    success_url = reverse_lazy('resident_list')

class ResidentDeleteView(DeleteView):
    model = Resident
    template_name = 'app/resident_delete.html'
    success_url = reverse_lazy('resident_list')