from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import Client
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def login(self):

        user = User.objects.create(username='mxa1101')
        user.set_password('Skyemage.213')
        user.save()

        c = Client()
        logged_in = c.login(username='mxa1101', password='Skyemage.213')

    def test_check_title(self):
        self.browser.get('http://127.0.0.1:8000/blog')

        self.assertIn('Abdulhannan Ahmad', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Blog Posts', header_text)
        
    def test_can_add_new_post(self):
        self.browser.get('http://127.0.0.1:8000/post/new/')

        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('New post', header_text)

        input_title = self.browser.find_element_by_id('id_title')
        input_title.send_keys('Functional Test Title')

        input_text = self.browser.find_element_by_id('id_text')
        input_text.send_keys('Functional Test Text')

        input_description = self.browser.find_element_by_id('id_description')
        input_description.send_keys('Functional Test Description')

        input_title.send_keys(Keys.ENTER)
        time.sleep(10)

        title = self.browser.find_element_by_tag_name('h2').text
        print("TITLE ", title)
        self.assertTrue(input_title, title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
        
