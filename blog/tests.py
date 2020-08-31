from django.test import TestCase
from django.urls import resolve
from blog.views import resume, home
from django.http import HttpRequest
from django.template.loader import render_to_string

class TemplateTests(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    # test if templates return correct html 
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/home') 
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_post_list_returns_corrent_html(self):
        response = self.client.get('/blog')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_new_returns_correct_html(self):
        response = self.client.get('/post/new/')
        self.assertTemplateUsed(response, 'blog/post_edit.html')

    def test_resume_page_returns_correct_html(self):
        response = self.client.get('/resume')
        self.assertTemplateUsed(response, 'blog/resume.html')

    def test_work_experience_new_returns_correct_html(self):
        response = self.client.get('/work_experience_new')
        self.assertTemplateUsed(response, 'blog/work_experience_edit.html')

    def test_education_new_returns_correct_html(self):
        response = self.client.get('/education_new')
        self.assertTemplateUsed(response, 'blog/education_edit.html')
    
    def test_interest_new_returns_correct_html(self):
        response = self.client.get('/interest_new')
        self.assertTemplateUsed(response, 'blog/interest_edit.html')



