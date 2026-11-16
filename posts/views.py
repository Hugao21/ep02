from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import CategoryForm, CommentForm, PostForm
from .models import Category, Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = ['-pub_date']


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'

    def get_success_url(self):
        return reverse('posts:detail', args=(self.object.id, ))


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'

    def get_success_url(self):
        return reverse('posts:detail', args=(self.object.id, ))


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:index')


def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/comment.html', context)


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'posts/categories.html'
    ordering = ['name']


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'posts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = self.object.posts.order_by('-pub_date')
        return context


class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'posts/category_create.html'

    def get_success_url(self):
        return reverse('posts:category', args=(self.object.id, ))
