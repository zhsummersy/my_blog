from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all().order_by('-slug')#all in a query set
    context = {'allPosts' : allPosts}
    return render(request,'blog/blogHome.html', context)
    #return HttpResponse("This is blogHome")
def blogPost(request,pk):
    post = Post.objects.filter(pk=pk).latest('timeStamp')
    print(post)
    context = {'post':post}

    return render(request,'blog/blogPost.html', context)
    #return HttpResponse(f'This is blogPost:{slug}')



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Eror - User not getting Authenticated
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Eror End

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f':Your account has been created! You are now able to log in ')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'blog/register.html',{'form':form})

# @login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f':Your account has been Updated ')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'blog/profile.html', context)
    