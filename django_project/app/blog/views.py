from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Post, Announce, Poll, Event
from .utils import Calendar
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CreatePollForm, EventForm
from django.urls import reverse_lazy
from datetime import datetime, date, timedelta
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})

# Homepage CRUD

@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

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

# Announcement CRUD

@login_required
def announcement(request):
    context = {
        'announcements': Announce.objects.all()
    }
    return render(request, 'blog/announcement.html', context)

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
    
# Hang-out ideas Poll CRUD

@login_required
def hangout_ideas(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'blog/hangout_ideas.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hangout-ideas')
    form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'blog/create_poll.html', context)

@login_required
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid Form')
        
        poll.save()

        return redirect('result-poll', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'blog/vote_poll.html', context)

@login_required
def result(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'blog/result_poll.html', context)

def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    poll.delete()
    return redirect('hangout-ideas')

# Hang-out schedule CRUD


@login_required
def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'blog/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        url = reverse('my-calendar')
        return HttpResponseRedirect(url)
    return render(request, 'blog/event.html', {'form': form})

# Bucket List

@login_required
def bucketlist(request):
    return render(request, 'blog/bucketlist.html', {'title': 'Bucket-Lists'})

