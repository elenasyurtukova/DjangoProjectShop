from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Post

class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ['name', 'content', 'image']
    success_url = reverse_lazy('blog:posts_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['name', 'content', 'image']
    success_url = reverse_lazy('blog:posts_list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts_list')