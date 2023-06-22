from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    approved_comments = post.comments.filter(approved=True).order_by('created_on')
    return render(
        request,
        'post_detail.html',
        {
            'post': post,
            'comments': approved_comments,
            'comment_form': CommentForm()
        },
    )
