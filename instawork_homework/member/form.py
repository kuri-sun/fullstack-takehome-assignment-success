from django.forms import ModelForm, RadioSelect, TextInput
from .models import Member

# Create your models' form

class MemberForm(ModelForm):
  class Meta:
    model = Member
    fields = '__all__'
    role_choices = [('0', "Regular - Can't delete members"), ('1', "Admin - Can delete members")]
    widgets = {
        'first_name': TextInput(attrs={'required': False, 'class':'form-control', 'placeholder':'First Name'}),
        'last_name': TextInput(attrs={'required': False, 'class': 'form-control', 'placeholder': 'Last Name'}),
        'email': TextInput(attrs={'required': False, 'class': 'form-control', 'placeholder': 'Email'}),
        'role': RadioSelect(),
        'phone_number': TextInput(attrs={'required': False, 'class': 'form-control', 'placeholder': 'Phone Number'}),
    }
