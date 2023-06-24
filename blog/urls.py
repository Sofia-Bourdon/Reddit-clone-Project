from . import views 
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/', views.comment_post, name='comment_post')
]

