from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Subreddit, Profile, UserActivity, Comment
from .forms import CommentForm, PostForm, ProfileForm


class PostList(generic.ListView):
    """Display an organized list of posts that are published."""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('upvotes')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subreddits'] = Subreddit.objects.all()
        context['post_form'] = PostForm()
        return context


@login_required
def post_detail(request, pk):
    """Show details for a single post, including comments and voting."""
    post = get_object_or_404(Post, pk=pk)
    approved_comments = post.comments.filter(
        approved=True).order_by('created_on')
    subreddits = Subreddit.objects.all()
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if 'upvote' in request.POST:
            handle_upvote(request, post)
        elif 'downvote' in request.POST:
            handle_downvote(request, post)
        elif form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)

    edit_form = PostForm(instance=post)

    return render(
        request,
        'post_detail.html',
        {
            'post': post,
            'comments': approved_comments,
            'comment_form': form,
            'edit_form': edit_form,
            'subreddits': subreddits,
        },
    )


def handle_upvote(request, post):
    """Process an upvote for a post."""
    if request.user.is_authenticated:
        if request.user in post.upvotes.all():
            post.upvotes.remove(request.user)
        else:
            post.upvotes.add(request.user)
            post.downvotes.remove(request.user)
    else:
        return redirect('login')


def handle_downvote(request, post):
    """Process a downvote for a post."""
    if request.user.is_authenticated:
        if request.user in post.downvotes.all():
            post.downvotes.remove(request.user)
        else:
            post.downvotes.add(request.user)
            post.upvotes.remove(request.user)
    else:
        return redirect('login')


def comment_post(request, slug):
    """Allow users to comment on a post."""
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
            messages.success(request, 'Your comment is waiting for approval!')
            UserActivity.objects.create(
                user=request.user, action_type='comment_created')

    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'form': form})


def delete_comment(request, pk):
    """Allow users to delete their own posts."""
    comment = get_object_or_404(comment, pk=pk)
    if comment.author == request.user and request.method == 'POST':
        comment.delete()
        messages.success(request, 'Your comment was successfully deleted!')
    return redirect('home')


@login_required
def subreddit(request, slug):
    """Show posts for a specific subreddit and allow new post submissions."""
    subreddit = get_object_or_404(Subreddit, slug=slug)
    posts = Post.objects.filter(subreddit=subreddit)
    subreddits = Subreddit.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.subreddit = subreddit
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(
        request,
        'subreddit.html',
        {
            'subreddit': subreddit,
            'post_form': form,
            'posts': posts,
            'subreddits': subreddits,
        },
    )


@login_required
def make_new_post(request):
    """Provide a form for submitting a new post."""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Your post was created successfully!')
            return redirect('post_detail', pk=new_post.pk)
            UserActivity.objects.create(
                user=request.user, action_type='post_created')
    else:
        return redirect('home')


def delete_post(request, slug):
    """Allow users to delete their own posts."""
    post = get_object_or_404(Post, slug=slug, status=1)
    if post.author == request.user and request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post was successfully deleted!')
    return redirect('home')


@login_required
def edit_post(request, pk):
    """ A view to allow the user to edit his own post"""
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user and request.method == 'POST':
        edit_form = PostForm(request.POST, instance=post)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', pk=pk)
        else:
            messages.error(
                request, 'Failed to update post. Please try again.')
    else:
        edit_form = PostForm(instance=post)

    return render(request, 'post_detail.html', {'edit_form': edit_form, 'post': post})


@login_required
def profile(request):
    """Display and edit the user's profile and show their activities."""
    posts = Post.objects.filter(author=request.user)
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,
                           instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileForm(instance=request.user.profile)

    activities = UserActivity.objects.filter(
        user=request.user).order_by('-timestamp')

    return render(
        request,
        'profile.html',
        {
            'profile': profile,
            'form': form,
            'activities': activities,
            'posts': posts,
        },
    )
