from django import forms
from .models import Post, Experience, Education, Interest
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','description','text',)

class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('experience_title','location','description',)
        labels = {
            'experience_title' : 'Job Title',
            'location' : 'Location',
            'description' : 'Experience Description',
        }

class EducationForm(forms.ModelForm):
    
    class Meta:
        model = Education
        fields = ('education_level','institute','results',)
        labels = {
            'education_level' : 'Education Level',
            'institute' : 'Institution',
            'results' : 'Results',
        }

class InterestsForm(forms.ModelForm):
    
    class Meta:
        model = Interest
        fields = ('interest','description',)
        labels = {
            'interest' : 'Interest',
            'description' : 'Interest Description',
        }



