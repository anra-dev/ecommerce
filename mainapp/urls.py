from django.urls import path
from .views import test_view, ProductDetailView


urlpatterns = [
    path('', test_view, name='base'),
    path('product/<str:ct_model>/<str:slag>/', ProductDetailView.as_view(), name='product_detail')
]