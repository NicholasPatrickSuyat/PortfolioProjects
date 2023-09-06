from django.shortcuts import render, get_object_or_404
from .models import Post, Announce
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

@login_required
def bucketlist(request):
    return render(request, 'blog/bucketlist.html', {'title': 'Bucket-Lists'})

@login_required
def announcement(request):
    context = {
        'announcements': Announce.objects.all()
    }
    return render(request, 'blog/announcement.html', context)


@login_required
def hangout_ideas(request):
    return render(request, 'blog/hangout_ideas.html', {'title': 'hangout_ideas'})

@login_required
def hangout_schedule(request):
    return render(request, 'blog/hangout_schedule.html', {'title': 'hangout_schedule'})

@login_required
def ranting_page(request):
    return render(request, 'blog/ranting.html', {'title': 'ranting_page'})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

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
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class UserAnnounceListView(LoginRequiredMixin, ListView):
    model = Announce
    template_name = 'blog/user_announce.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'announcements'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class AnnounceListView(LoginRequiredMixin, ListView):
    model = Announce
    template_name = 'blog/announcement.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'announcements'
    ordering = ['-date_posted']
    paginate_by = 5

class AnnounceDetailView(LoginRequiredMixin, DetailView):
    model = Announce

class AnnounceCreateView(LoginRequiredMixin, CreateView):
    model = Announce
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class AnnounceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announce
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class AnnounceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announce
    success_url = "/announcement/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False