from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig

from catalog.views import contacts, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, \
    CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('list/', CategoryListView.as_view(), name='list_category'),
]