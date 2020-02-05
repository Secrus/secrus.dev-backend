from django.shortcuts import render
from .models import BlogPost
from datetime import datetime


def post_list(request):
    posts = BlogPost.objects.filter(publication_date__lte = datetime.now()).order_by('publication_date')
    return render(request, 'blog/post_list.html', {
        'posts': posts,
    })


def main_page(request):
    return render(request, 'blog/main.html', {})