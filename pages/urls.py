from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('simbol-emoji/', views.simbolemoji, name='simbolemoji'),
    path('text-convert/', views.textconvert, name='textconvert'),
    path('your-name/', views.get_name, name='your_name'),
    path('thanks/', views.get_name, name='your_name'),
]
