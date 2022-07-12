from django.shortcuts import render
from .models import Member

# Create your views here.

def listPage(request):
  members = Member.objects.all()

  context = {'members': members}
  return render(request, 'list.html', context)