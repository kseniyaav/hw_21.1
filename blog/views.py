from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Article


class BlogListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body', 'preview')
    # success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:view_article', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:list')