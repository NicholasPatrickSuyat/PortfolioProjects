from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, AnnounceListView, UserAnnounceListView, AnnounceDetailView, AnnounceCreateView, AnnounceUpdateView, AnnounceDeleteView
from . import views
from . import views as blog_views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('announcement/', AnnounceListView.as_view(), name='announcement'),
    path('user/announce/<str:username>', UserAnnounceListView.as_view(), name='user-announcements'),
    path('announce/<int:pk>/', AnnounceDetailView.as_view(), name='announce-detail'),
    path('announce/new/', AnnounceCreateView.as_view(), name='announce-create'),
    path('announce/<int:pk>/update/', AnnounceUpdateView.as_view(), name='announce-update'),
    path('announce/<int:pk>/delete/', AnnounceDeleteView.as_view(), name='announce-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('bucketlist/', blog_views.bucketlist, name='bucket-list'),
    path('hangout_ideas/', blog_views.hangout_ideas, name='hangout-ideas'),
    path('hangout_schedule/', blog_views.hangout_schedule, name='hangout-schedule'),
    path('ranting_page/', blog_views.ranting_page, name='ranting'),
    
]
