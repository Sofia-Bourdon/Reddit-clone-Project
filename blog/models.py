from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS_CHOICES = (
    (0, "Draft"),
    (1, "Published"),
)

ACTION_CHOICES = (
    ('post_created', 'Post Created'),
    ('comment_created', 'Comment Created'),
    ('post_upvoted', 'Post Upvoted'),
    ('post_downvoted', 'Post Downvoted'),
    ('comment_upvoted', 'Comment Upvoted'),
    ('comment_downvoted', 'Comment Downvoted'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} - {self.get_action_type_display()}"


class Subreddit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    subscribers = models.ManyToManyField(
        User, related_name='subscribed_subreddits', blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    upvotes = models.ManyToManyField(
        User, related_name='post_upvotes', blank=True, related_query_name='post_upvote')
    downvotes = models.ManyToManyField(
        User, related_name='post_downvotes', blank=True, related_query_name='post_downvote')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_upvotes(self):
        return self.upvotes.count()

    def number_of_downvotes(self):
        return self.downvotes.count()

    def total_votes(self):
        return self.number_of_upvotes() - self.number_of_downvotes()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    upvotes = models.ManyToManyField(
        User, related_name='comment_upvotes', blank=True, related_query_name='comment_upvote')
    downvotes = models.ManyToManyField(
        User, related_name='comment_downvotes', blank=True, related_query_name='comment_downvote')

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def number_of_upvotes(self):
        return self.upvotes.count()

    def number_of_downvotes(self):
        return self.downvotes.count()


def get_posts_ordered_by_votes():
    from .models import Post
    posts = Post.objects.annotate(
        total_votes=models.Count('upvotes') - models.Count('downvotes')
    ).order_by('-total_votes', '-created_on')
    return posts
