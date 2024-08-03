from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from editor.models import Publications


class EditorCreateView(CreateView):
    model = Publications
    fields = ('title', 'preview', 'body')
    success_url = reverse_lazy('editor:list')


class EditorListView(ListView):
    model = Publications


class EditorDetailView(DetailView):
    model = Publications
    template_name = 'editor/publications_detail.html'