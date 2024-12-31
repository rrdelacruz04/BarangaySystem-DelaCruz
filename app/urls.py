from django.contrib.admin.templatetags.admin_list import pagination_tag
from django.urls import path
from .views import HomePageView, AboutPageView 
from .views import (
    ResidentListView, 
    ResidentDetailView, 
    ResidentCreateView,
    ResidentUpdateView,
    ResidentDeleteView, 

)





urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    
    path('resident/', ResidentListView.as_view(), name='resident'),    
    path('resident/<int:pk>/', ResidentDetailView.as_view(), name='resident_detail'),
    path('resident/create/', ResidentCreateView.as_view(), name='resident_create'),
    path('resident/update/<int:pk>/', ResidentUpdateView.as_view(), name='resident_update'),
    path('resident/delete/<int:pk>/', ResidentDeleteView.as_view(), name='resident_delete'),
    path('resident/', ResidentListView.as_view(), name='resident_list'),
   


   
]