from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProducDetailView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name



urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>', ProducDetailView.as_view(), name='view'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]
