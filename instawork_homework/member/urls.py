from django.urls import path
from . import views

urlpatterns = [
  path('', views.homePage, name='home'),
  path('add/', views.addMember, name='add'),
  path('edit/<str:pk>', views.editMember, name='edit'),
  path('delete/<str:pk>', views.deleteMember, name='delete')
]