from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Experience, Education, Interest
from .forms import PostForm, ExperienceForm, EducationForm, InterestsForm
from django.http import  HttpResponse
from django.db.models import CharField
from django.db.models import Value

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)


    else:
        form = PostForm

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# def resume(request):
#     return render(request, 'blog/resume.html')

def work_experience_new(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('resume')


    else:
        form = ExperienceForm

    return render(request, 'blog/work_experience_edit.html', {'form': form})

def education_new(request):
    if request.method == "POST":
        form = EducationForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('resume')


    else:
        form = EducationForm

    return render(request, 'blog/education_edit.html', {'form': form})

def interest_new(request):
    if request.method == "POST":
        form = InterestsForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('resume')


    else:
        form = InterestsForm

    return render(request, 'blog/interest_edit.html', {'form': form})

def resume(request):
    experiences = Experience.objects.all().annotate(type=Value('experience', CharField())).order_by('-published_date')
    educations = Education.objects.all().annotate(type=Value('education', CharField())).order_by('-published_date')
    interests = Interest.objects.all().annotate(type=Value('interest', CharField()))


    all_items = list(experiences) + list(educations) + list(interests)

    return render(request, 'blog/resume.html', {'all_items_feed': all_items})

    # posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')

# def experience_list(request):
#     experiences = Experience.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
#     return render(request, 'resume.html', {'experiences' : experiences})

# def education_list(request):
#     educations = Education.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
#     return render(request, 'resume.html', {'educations' : educations})

# def interest_list(request):
#     interests = Interest.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
#     return render(request, 'resume.html', {'interests' : interests})


