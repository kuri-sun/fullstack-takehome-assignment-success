from django.test import TestCase
from member.models import Member


class TestModels(TestCase):

  def setUp(self):
    self.member1 = Member.objects.create(
      first_name='first',
      last_name='last',
      email='user@gmail.com',
      phone_number='2221113333',
      role=0
    )

  
  def test_phone_number_text(self):
    self.assertEquals(self.member1.phone_number_text(), '222-111-3333')  


  def test_role_text_regular(self):
    self.assertEquals(self.member1.role_text(), '')


  def test_role_text_admin(self):
    self.member1.role = 1
    self.assertEquals(self.member1.role_text(), ' (admin)')