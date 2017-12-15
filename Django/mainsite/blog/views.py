from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost, Comment
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    if request.method == 'POST':
        user = request.POST['user_name']
        password = request.POST['user_password']
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)

    blogs = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

def detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST' and request.user.is_authenticated:
        body = request.POST['body']
        comment = Comment(user=request.user, body=body, post=post)                   #comments not working correctly
        comment.save()
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/detailedBlog.html', context)


@login_required
@permission_required('blog.add_blog', raise_exception=True)
def createBlog(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        body = request.POST['body']
        blog = BlogPost(user=user, title=title, body=body)
        blog.save()
        return HttpResponseRedirect(reverse('blog:index'))
    return render(request, 'blog/newBlog.html')


def registration(request):
    if request.method == 'POST':
        user = request.POST['user_name']  # can i duplicate this?
        email = request.POST['user_email']
        password = request.POST['user_password']
        user = User.objects.create_user(user, email, password)
        group = get_object_or_404(Group, name='Commenters')
        group.user_set.add(user)
        return HttpResponseRedirect(reverse('blog:index'))
    return render(request, 'blog/create.html')

def blogComment(request):
    user = request.POST['user']
    body = request.POST['body']
    comments = Comment(user=user, body=body)
    comments.save()
    return render(request, 'blog/detailedBlog.html', {'comments': comments})


