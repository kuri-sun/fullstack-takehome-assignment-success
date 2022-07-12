from django.shortcuts import render, redirect, get_object_or_404
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


def addMember(request):
    """
    render form.html page when user access to "/add"

    :request http request object.
    :return http response to render form.html to user's browser.
    """ 
    page = 'add'

    if request.method == 'POST':
      form = MemberForm(request.POST) 
      if form.is_valid():
        form.save() # save to db
        return redirect('home') # push to home.html
      else:
        context = {'page': page, 'form': form, 'errors': dict(form.errors) }
        return render(request, 'instawork_homework/form.html', context) # push same page again with error message.
    else:
      context = {'page': page, 'form': MemberForm()}
      return render(request, 'instawork_homework/form.html', context)


def editMember(request, pk):
    """
    render form.html page when user access to "/edit"

    :request http request object.
    :pk primary key for Member object.
    :return http response to render form.html to user's browser.
    """ 
    page = 'edit'
    member = get_object_or_404(Member, id=pk)
    form = MemberForm(instance=member)

    if request.method == 'POST':
      # POST request 
      form = MemberForm(request.POST, instance=member)
      if form.is_valid():
        form.save() # update db Member data
        return redirect('home') # push to home.html
      else:
        context = {'page': page, 'form': form, 'errors': dict(form.errors) }
        return render(request, 'instawork_homework/form.html', context) # push same page again with error message.
    else:
      # GET request 
      context = {'page': page, 'form': form, 'member': member}
      return render(request, 'instawork_homework/form.html', context)


def deleteMember(request, pk):
    """
    user click delete button to delete a user.

    :request http request object.
    :pk primary key for Member object.
    :return http response to render form.html to user's browser.
    """ 
    member = get_object_or_404(Member, id=pk)
    member.delete()
    return redirect('home')
