from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('blog', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # resume stuff
    path('resume', views.resume, name='resume'),
    # path('experience_list', views.experience_list, name = 'resume'),
    # path('education_list', views.education_list, name = 'resume'),
    # path('interest_list', views.interest_list, name = 'resume'),

    path('work_experience_new', views.work_experience_new, name='work_experience_new'),
    path('education_new', views.education_new, name='education_new'),
    path('interest_new', views.interest_new, name='interest_new'),

    path('work_experience_edit/<int:pk>', views.work_experience_edit, name='work_experience_edit'),
    path('education_edit/<int:pk>', views.education_edit, name='education_edit'),
    path('interest_edit/<int:pk>', views.interest_edit, name='interest_edit'),


]

