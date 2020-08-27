from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('', PostListView.as_view(), name="blog-home"),  # if .as_view (emty) it will look for <app>/<model>_<veiwtype>.html in this case -> blog/post_list.html
    path('about/', views.about, name="blog-about"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # integer of primery key
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]
