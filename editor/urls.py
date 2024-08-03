from django.urls import path
from editor.apps import EditorConfig
from editor.views import EditorCreateView, EditorListView, EditorDetailView, EditorUpdateView, EditorDeleteView, \
    toggle_published

app_name = EditorConfig.name



urlpatterns = [
    path('', EditorListView.as_view(), name='list'),
    path('create/',EditorCreateView.as_view(), name='create'),
    path('view/<int:pk>', EditorDetailView.as_view(), name='view'),
    path('edit/<int:pk>', EditorUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', EditorDeleteView.as_view(), name='delete'),
    path('published/<int:pk>', toggle_published, name='toggle_published')
]
