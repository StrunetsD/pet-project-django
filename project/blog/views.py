from django.shortcuts import render, get_object_or_404
from .models import Blog

def post_list(request):
    posts = Blog.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'post_detail.html', {'post': post})