import os, sys
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings") 
import django
django.setup()

from django.contrib.auth.models import User
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from django.test import Client, TestCase
import unittest
import time

def login(self):
    self.browser.get('http://127.0.0.1:8000/admin/login/?next=/admin/')


    input_username = self.browser.find_element_by_name('username')
    input_username.send_keys('testuser')

    input_password = self.browser.find_element_by_name('password')
    input_password.send_keys('12345')

    element = self.browser.find_element_by_class_name("submit-row")
    ActionChains(self.browser).click(element).perform()

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'chromedriver.exe')

        self.user1 = User.objects.create_superuser(username='testuser', email='user@test.com',password='12345')

    def tearDown(self):
        self.browser.quit()
        self.user1.delete()

    def test_login(self):
        self.browser.get('http://127.0.0.1:8000/admin/login/?next=/admin/')

        input_username = self.browser.find_element_by_name('username')
        input_username.send_keys('testuser')

        input_password = self.browser.find_element_by_name('password')
        input_password.send_keys('12345')

        element = self.browser.find_element_by_class_name("submit-row")
        ActionChains(self.browser).click(element).perform()

        self.assertIn('Site administration | Django site admin', self.browser.title)

    def test_check_title(self):
        self.browser.get('http://127.0.0.1:8000/blog')

        self.assertIn('Abdulhannan Ahmad', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Blog Posts', header_text)


    def test_can_add_new_post(self):
        login(self)
        self.browser.get('http://127.0.0.1:8000/post/new/')
        
        self.assertIn('Abdulhannan Ahmad', self.browser.title)

        input_title = self.browser.find_element_by_id('id_title')
        input_title.send_keys('unit test')

        input_text = self.browser.find_element_by_id('id_text')
        input_text.send_keys('unit test2')

        time.sleep(2)

        element = self.browser.find_element_by_css_selector(".btn-default")
        ActionChains(self.browser).click(element).perform()

        self.assertTrue(input_title, self.browser.find_element_by_tag_name('h2'))
        self.assertTrue(input_text, self.browser.find_element_by_tag_name('p'))



if __name__ == '__main__':
    unittest.main(warnings='ignore')
        
