from django import forms
from .models import Comment, Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('body', rows="3", css_class='form-control'),
            Submit('submit', 'Post Comment', css_class='btn btn-primary mt-2')
        )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'slug', 'subreddit')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('title', css_class='form-control'),
            Field('content', css_class='form-control'),
            Field('slug', css_class='form-control'),
            Field('subreddit', css_class='form-control'),
            Submit('submit', 'Submit Post', css_class='btn btn-primary mt-2')
        )
