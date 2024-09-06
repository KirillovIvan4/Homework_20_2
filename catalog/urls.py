from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProducDetailView, ProductUpdateView, ProductDeleteView, \
    ProductCreateView

app_name = CatalogConfig.name



urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name='list'),
    path('create/',ProductCreateView.as_view(), name='create'),
    path('view/<int:pk>', ProducDetailView.as_view(), name='view'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]
