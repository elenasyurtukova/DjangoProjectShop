from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Post

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_publicated=True)


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ['name', 'content', 'image', 'is_publicated']
    success_url = reverse_lazy('blog:posts_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['name', 'content', 'image', 'is_publicated']
    success_url = reverse_lazy('blog:posts_list')

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts_list')