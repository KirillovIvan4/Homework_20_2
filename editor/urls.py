from django.urls import path
from editor.apps import EditorConfig
from editor.views import EditorCreateView
app_name = EditorConfig.name



urlpatterns = [
   # path('', ...., name='list'),
    path('create/',EditorCreateView.as_view(), name='create'),
  #  path('view/<int:pk>', ..., name='view'),
   # path('edit/<int:pk>', ..., name='edit'),
   # path('delete/<int:pk>', ..., name='delete')
]
