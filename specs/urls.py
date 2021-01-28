from django.urls import path

from .views import BaseSpecView, NewCategoryView, NewFeatureView

urlpatterns = [
    path('', BaseSpecView.as_view(), name='base-spec'),
    path('new-category/', NewCategoryView.as_view(), name='new-category'),
    path('new-feature/', NewFeatureView.as_view(), name='new-feature')
]