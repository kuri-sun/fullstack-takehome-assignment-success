from django.test import SimpleTestCase
from member.form import MemberForm

class TestForms(SimpleTestCase):

  def test_member_form_valid_data(self):
    form = MemberForm(data={
      'first_name': 'updated',
      'last_name': 'last',
      'email': 'user@gmail.com',
      'phone_number': '2221113333',
      'role': 0
    })

    self.assertTrue(form.is_valid())


  def test_member_form_no_data(self):
    form = MemberForm(data={})

    self.assertFalse(form.is_valid())
    self.assertEquals(len(form.errors), 5)