from django.urls import path
from .views import MemberList, CreateMember, UpdateMember
from . import views

urlpatterns = [
  path('', MemberList.as_view(), name='home'),
  path('add/', CreateMember.as_view(), name='add'),
  path('edit/<str:pk>', UpdateMember.as_view(), name='edit'),
  path('delete/<str:pk>', views.deleteMember, name='delete')
]