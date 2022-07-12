from django.test import TestCase, Client
from django.urls import reverse
from member.models import Member
from member.form import MemberForm
import json

# test your views
class TestViews(TestCase):


  def setUp(self):
    '''
    everytime test cases are invoked.
    '''
    self.client = Client()
    self.member1 = Member.objects.create(
      first_name='first',
      last_name='last',
      email='user@gmail.com',
      phone_number='2221113333',
      role=0
    )
    self.home_url = reverse('home')
    self.add_url = reverse('add')
    self.edit_url = reverse('edit', args=['1'])
    self.delete_url = reverse('delete', args=['1'])


  def tearDown(self):
    '''
    everytime test cases are finished.
    '''
    Member.objects.all().delete()


  def test_home_page_GET(self):
    '''
    test for GET request to homePage view.
    '''
    response = self.client.get(self.home_url)

    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'instawork_homework/home.html')


  def test_add_page_GET(self):
    '''
    test for GET request to addPage view.
    '''
    response = self.client.get(self.add_url)

    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'instawork_homework/form.html')


  def test_add_page_POST(self):
    '''
    test for POST request to addPage view.
    '''
    response = self.client.post(self.add_url, {
      'first_name': 'first2',
      'last_name': 'last2',
      'email': 'user2@gmail.com',
      'phone_number': '2221113333',
      'role': 1,
    })

    self.assertEquals(response.status_code, 302)
    self.assertEquals(Member.objects.get(id='2').first_name, 'first2') # new member in DB


  def test_edit_page_GET(self):
    '''
    test for GET request to editPage view.
    '''
    response = self.client.get(self.edit_url)

    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'instawork_homework/form.html')


  def test_edit_page_POST(self):
    '''
    test for POST request to editPage view.
    '''
    response = self.client.post(self.edit_url, {
      'first_name': 'updated',
      'last_name': 'last',
      'email': 'user@gmail.com',
      'phone_number': '2221113333',
      'role': 0,
    })

    self.assertEquals(response.status_code, 302)
    self.assertEquals(Member.objects.get(id='1').first_name, 'updated') # member whose id is '1' is updated 


  def test_delete_page_GET(self):
    '''
    test for GET request to deletePage view.
    '''
    response = self.client.get(self.delete_url)
    self.assertEquals(response.status_code, 302)
    self.assertEquals(Member.objects.all().count(), 0) # there is no member in DB