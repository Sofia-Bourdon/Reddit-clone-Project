from . import views 
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/', views.comment_post, name='comment_post'),
    path('r/<slug:slug>/', views.subreddit, name='subreddit'),
    path('<slug:slug>/', views.make_new_post, name='make_new_post'),
    path('delete-post/<slug:slug>/', views.delete_post, name='delete_post'),
]
