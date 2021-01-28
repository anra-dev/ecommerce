from django.shortcuts import render, HttpResponseRedirect
from django.views import View

from .forms import NewCategoryForm, NewCategoryFeatureKeyForm

class BaseSpecView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'product_features.html', {})


class NewCategoryView(View):

    def get(self, request, *args, **kwargs):
        form = NewCategoryForm(request.POST or None)
        context = {'form': form}
        return render(request, 'new_category.html', context)

    def post(self, request, *args, **kwargs):
        form = NewCategoryForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product-specs/')
        return render(request, 'new_category.html', context)


class NewFeatureView(View):

    def get(self, request, *args, **kwargs):
        form = NewCategoryFeatureKeyForm(request.POST or None)
        context = {'form': form}
        return render(request, 'new_feature.html', context)

    def post(self, request, *args, **kwargs):
        form = NewCategoryFeatureKeyForm(request.POST or None)
        if form.is_valid():
            new_category_featute_key = form.save(commit=False)
            new_category_featute_key.category = form.cleaned_data['category']
            new_category_featute_key.feature_name = form.cleaned_data['feature_name']
            new_category_featute_key.save()
            return HttpResponseRedirect('/product-specs/')
        context = {'form': form}
        return render(request, 'new_feature.html', context)
