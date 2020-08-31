import os, sys
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings") 
import django
django.setup()

from blog.models import Post
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

class AddingAndEditingTests(unittest.TestCase):

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

    
    def test_can_add_new_workexperience(self):
        login(self)
        self.browser.get('http://127.0.0.1:8000/work_experience_new')

        input_job_title = self.browser.find_element_by_id('id_experience_title')
        input_job_title.send_keys('job title')
        input_location = self.browser.find_element_by_id('id_location')
        input_location.send_keys('location')
        input_experience = self.browser.find_element_by_id('id_description')
        input_experience.send_keys('experience')

        time.sleep(2)

        element = self.browser.find_element_by_css_selector(".btn-default")
        ActionChains(self.browser).click(element).perform()

        self.assertTrue(input_job_title, self.browser.find_element_by_tag_name('h2'))
        self.assertTrue(input_location, self.browser.find_element_by_tag_name('p'))
        self.assertTrue(input_experience, self.browser.find_element_by_tag_name('p'))


    def test_can_add_new_education(self):
        login(self)
        self.browser.get('http://127.0.0.1:8000/education_new')

        input_education_level = self.browser.find_element_by_id('id_education_level')
        input_education_level.send_keys('education level')
        input_institution = self.browser.find_element_by_id('id_institute')
        input_institution.send_keys('institution')
        input_results = self.browser.find_element_by_id('id_results')
        input_results.send_keys('results')

        time.sleep(2)

        element = self.browser.find_element_by_css_selector(".btn-default")
        ActionChains(self.browser).click(element).perform()

        self.assertTrue(input_education_level, self.browser.find_element_by_tag_name('h2'))
        self.assertTrue(input_institution, self.browser.find_element_by_tag_name('p'))
        self.assertTrue(input_results, self.browser.find_element_by_tag_name('p'))

    def test_can_add_new_interest(self):
        login(self)
        self.browser.get('http://127.0.0.1:8000/interest_new')

        input_interest = self.browser.find_element_by_id('id_interest')
        input_interest.send_keys('interest')
        input_description = self.browser.find_element_by_id('id_description')
        input_description.send_keys('description')

        time.sleep(2)

        element = self.browser.find_element_by_css_selector(".btn-default")
        ActionChains(self.browser).click(element).perform()

        self.assertTrue(input_interest, self.browser.find_element_by_tag_name('h2'))
        self.assertTrue(input_description, self.browser.find_element_by_tag_name('p'))



if __name__ == '__main__':
    unittest.main(warnings='ignore')
        
