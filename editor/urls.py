from django.urls import path
from editor.apps import EditorConfig
from editor.views import EditorCreateView, EditorListView, EditorDetailView
app_name = EditorConfig.name



urlpatterns = [
    path('', EditorListView.as_view(), name='list'),
    path('create/',EditorCreateView.as_view(), name='create'),
    path('view/<int:pk>', EditorDetailView.as_view(), name='view'),
   # path('edit/<int:pk>', ..., name='edit'),
   # path('delete/<int:pk>', ..., name='delete')
]
