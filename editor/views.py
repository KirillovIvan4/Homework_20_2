

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from django.contrib.auth.mixins import LoginRequiredMixin

from editor.models import Publications


class EditorCreateView(CreateView, LoginRequiredMixin):
    model = Publications
    fields = ('title', 'preview', 'body')
    success_url = reverse_lazy('editor:list')

    def form_valid(self, form):
        new_mat = form.save()
        new_mat.slug = slugify(new_mat.title)
        new_mat.save()

        editor = form.save()
        user = self.request.user
        editor.author = user
        editor.save()
        return super().form_valid(form)


class EditorListView(ListView):
    model = Publications

    def get_queryset(self):
        return Publications.objects.filter(is_published=True)

class EditorDetailView(DetailView):
    model = Publications
    template_name = 'editor/publications_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class EditorUpdateView(UpdateView, LoginRequiredMixin):
    model = Publications
    fields = ('title', 'preview', 'body')

    def form_valid(self, form):
        new_mat = form.save()
        new_mat.slug = slugify(new_mat.title)
        new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('editor:view', args=[self.kwargs.get('pk')])


class EditorDeleteView(DeleteView, LoginRequiredMixin):
    model = Publications
    success_url = reverse_lazy('editor:list')


def toggle_published(request, pk):
    publication_item = get_object_or_404(Publications, pk=pk)
    if publication_item.is_published:
        publication_item.is_published = False
    else:
        publication_item.is_published = True

    publication_item.save()

    return redirect(reverse('editor:list'))
