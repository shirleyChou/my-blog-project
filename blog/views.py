#!/usr/bin/activate
#encoding: utf-8

from django.shortcuts import render_to_response, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import RequestContext

from .models import Post
from .forms import PostForm

def _query_pages(request, pagination=False, **kwargs):
    blog_list = get_list_or_404(Post.objects.order_by('-publish_time'), **kwargs)
    if pagination:
        paginator = Paginator(blog_list, 10)
        page_num = request.GET.get('p', 1)
        try:
            contents = paginator.page(page_num)
        except PageNotAnInteger:
            page_num = 1
            contents = paginator.page(page_num)
        except EmptyPage:
            page_num = -1
            contents = paginator.page(paginator.num_pages)
        return contents, int(page_num)+1
    else:
        return blog_list


def home(request):
    posts, page_num = _query_pages(request, pagination=True)
    return render_to_response('home.html', {'posts': posts, 'page_num': page_num})

def all_posts(request):
    posts = _query_pages(request)
    return render_to_response('posts.html', {'posts': posts})

def article(request, blog_id, link=''):
    post = _query_pages(request, pk=blog_id)[0]
    return render_to_response('article.html', {'post': post})

def about_me(request):
    return render_to_response('about.html')

def page_not_found(request):
    return render_to_response('404.html')

"""   
def add_article(request):
    return render_to_response('new.html')
"""

def create_article(request):
    errors = []
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
        if 'title' in request.POST:
            q = request.POST.get('title')
            post = Post.objects.filter(title__icontains=q)
            return render_to_response(
                'article.html', 
                {'post': post},
                context_instance=RequestContext(request))
    return render_to_response('new.html')


    

