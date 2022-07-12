from django.urls import path
from . import views

urlpatterns = [
  path('', views.homePage, name='list'),
  path('add/', views.addPage, name='add'),
  path('edit/<str:pk>', views.editPage, name='edit'),
]