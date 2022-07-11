from django.shortcuts import render

# Create your views here.

def listPage(request):
  context = {}
  return render(request, 'list.html', context)