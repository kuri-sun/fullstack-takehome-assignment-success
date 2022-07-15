from django.test import SimpleTestCase
from django.urls import reverse, resolve
from member.views import MemberList, CreateMember, UpdateMember, deleteMember

# test your urls

class TestUrls(SimpleTestCase):

  def test_home_url_is_resolved(self):
    '''
    test for 'home url 
    '''
    url = reverse('home')
    self.assertEquals(resolve(url).func.view_class, MemberList)

  def test_add_url_is_resolved(self):
    '''
    test for 'add' url 
    '''
    url = reverse('add')
    self.assertEquals(resolve(url).func.view_class, CreateMember)
  
  def test_edit_url_is_resolved(self):
    '''
    test for 'edit' url 
    '''
    url = reverse('edit', args=['some-pk'])
    self.assertEquals(resolve(url).func.view_class, UpdateMember)
  
  def test_delete_url_is_resolved(self):
    '''
    test for 'delete' url 
    '''
    url = reverse('delete', args=['some-pk'])
    self.assertEquals(resolve(url).func, deleteMember)