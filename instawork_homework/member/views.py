from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Member
from .form import MemberForm
from django.contrib import messages

# Create your views here.

class MemberList(ListView):
  """
  render home.html page when user access to "/"
  """ 
  model = Member
  context_object_name = 'members'
  template_name = 'member/home.html'


class CreateMember(CreateView):
  """
  render form.html page when user access to "/add"
  """ 
  model = Member
  form_class = MemberForm
  template_name = 'member/form.html'
  success_url = reverse_lazy('home')
  error_message = 'Error while saving, check your inputs.'

  def form_invalid(self, form):
    messages.error(self.request, self.error_message)
    return super().form_invalid(form)
  
  # set context
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page'] = 'add' # for create new member form
    return context


class UpdateMember(UpdateView):
  """
  render form.html page when user access to "/edit"
  """ 
  model = Member
  form_class = MemberForm
  template_name = 'member/form.html'
  success_url = reverse_lazy('home')
  error_message = 'Error while saving, check your inputs.'

  def form_invalid(self, form):
    messages.error(self.request, self.error_message)
    return super().form_invalid(form)

  # set context
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page'] = 'edit' # for update member form
    return context


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
