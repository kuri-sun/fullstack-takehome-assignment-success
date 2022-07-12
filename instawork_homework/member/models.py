from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Member(models.Model):
    # helper properties 
    ROLES = [
        (0, "Regular - Can't delete members"),
        (1, "Admin - Can delete members")
    ]
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Invalid phone number.")

    # columns
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=150, blank=False)
    role = models.IntegerField(choices=ROLES, default=0)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=False)


    # helper methods
    def phone_number_text(self):
      return str(self.phone_number[0:3] + "-" + self.phone_number[3:6] + "-" + self.phone_number[6:])
      
    def role_text(self):
      if self.role == 1:
        return " (admin)"
      else:
        return ""
