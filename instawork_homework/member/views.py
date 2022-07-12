from django.shortcuts import render, redirect
from .models import Member
from .form import MemberForm

# Create your views here.

def homePage(request):
    """
    render home.html page when user access to "/"

    :request http request object.
    :return GET http response to render home.html to user's browser.
    """ 

    members = Member.objects.all()
    members_count = members.count()
    context = {'members': members, 'members_count': members_count}
    return render(request, 'instawork_homework/home.html', context)


def addPage(request):
    """
    render form.html page when user access to "/add"

    :request http request object.
    :return http response to render form.html to user's browser.
    """ 
    page = 'add'
    roles = [
        (0, "Regular - Can't delete members"),
        (1, "Admin - Can delete members")
    ]

    if request.method == 'POST':
      form = MemberForm(request.POST) 
      if form.is_valid():
        form.save() # save to db
        return redirect('home') # push to home.html
      else:
        context = {'page': page, 'roles': roles, 'form': form, 'errors': dict(form.errors) }
        return render(request, 'instawork_homework/form.html', context) # push same page again with error message.
    else:
      context = {'page': page, 'roles': roles, 'form': MemberForm()}
      return render(request, 'instawork_homework/form.html', context)


def editPage(request, pk):
    """
    render form.html page when user access to "/edit"

    :request http request object.
    :return http response to render form.html to user's browser.
    """ 
    page = 'edit'
    roles = [
        (0, "Regular - Can't delete members"),
        (1, "Admin - Can delete members")
    ]
    member = Member.objects.get(id=pk)
    context = {'page': page, 'roles': roles, 'member': member}
    return render(request, 'instawork_homework/form.html', context)