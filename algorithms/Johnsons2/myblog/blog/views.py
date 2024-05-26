# blog/views.py
from django.shortcuts import render
# from .models import Post, Engineer
from .models import Engineer

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

def engineer_list(request):
    engineers = Engineer.objects.all()
    return render(request, 'blog/engineer_list.html', {'engineers': engineers})
