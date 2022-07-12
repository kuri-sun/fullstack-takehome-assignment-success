from django.test import SimpleTestCase
from django.urls import reverse, resolve
from member.views import homePage, addMember, deleteMember, editMember

# test your urls

class TestUrls(SimpleTestCase):

  def test_home_url_is_resolved(self):
    '''
    test for 'home url 
    '''
    url = reverse('home')
    self.assertEquals(resolve(url).func, homePage)

  def test_add_url_is_resolved(self):
    '''
    test for 'add' url 
    '''
    url = reverse('add')
    self.assertEquals(resolve(url).func, addMember)
  
  def test_edit_url_is_resolved(self):
    '''
    test for 'edit' url 
    '''
    url = reverse('edit', args=['some-pk'])
    self.assertEquals(resolve(url).func, editMember)
  
  def test_delete_url_is_resolved(self):
    '''
    test for 'delete' url 
    '''
    url = reverse('delete', args=['some-pk'])
    self.assertEquals(resolve(url).func, deleteMember)