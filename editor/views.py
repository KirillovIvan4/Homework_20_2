from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView


from editor.models import Publications


class EditorCreateView(CreateView):
    model = Publications
    fields = ('title', 'preview', 'body')
    #template_name = 'editor/blog.html'