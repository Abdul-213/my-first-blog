from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve
from blog.views import resume, home
from django.http import HttpRequest
from django.template.loader import render_to_string
from .models import Post

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

class PostTests(TestCase):

    def test_can_save_a_POST_request_blog(self):
        response_title = self.client.post('/post/new/', data={'title': 'a new title'})
        response_description = self.client.post('/post/new/', data={'description': 'this is a description'})
        response_text = self.client.post('/post/new/', data={'text': 'this is some text'})

        self.assertIn('a new title', response_title.content.decode())
        self.assertIn('this is a description', response_description.content.decode())
        self.assertIn('this is some text', response_text.content.decode())


    def test_can_save_a_POST_request_work_experience(self):
        response_title = self.client.post('/work_experience_new', data={'experience_title': 'an experience title'})
        response_location = self.client.post('/work_experience_new', data={'location': 'experience location'})
        response_exp_description = self.client.post('/work_experience_new', data={'description': 'experience description'})

        self.assertIn('an experience title', response_title.content.decode())
        self.assertIn('experience location', response_location.content.decode())
        self.assertIn('experience description', response_exp_description.content.decode())

    def test_can_save_a_POST_request_education(self):
        response_education_level = self.client.post('/education_new', data={'education_level': 'education level'})
        response_institution = self.client.post('/education_new', data={'institute': 'institution'})
        response_results = self.client.post('/education_new', data={'results': 'these results'})


        self.assertIn('education level', response_education_level.content.decode())
        self.assertIn('institution', response_institution.content.decode())
        self.assertIn('these results', response_results.content.decode())


    def test_can_save_a_POST_request_interests(self):
        response_interest = self.client.post('/interest_new', data={'interest': 'interest'})
        response_description = self.client.post('/interest_new', data={'description': 'interest description'})
        self.assertIn('interest', response_interest.content.decode())
        self.assertIn('interest description', response_description.content.decode())




