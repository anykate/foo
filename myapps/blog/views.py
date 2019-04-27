from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, ListView

from .forms import CommentForm
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def post(self, request, slug=None):
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse('blog:post_detail', kwargs={'slug': slug})
            )
        return self.get(request, slug=slug)

    def get_context_data(self, **kwargs):
        ctx = super(PostDetailView, self).get_context_data(**kwargs)
        ctx['form'] = CommentForm(
            initial={
                'post': self.object,
                'user': self.request.user
            }
        )
        return ctx
