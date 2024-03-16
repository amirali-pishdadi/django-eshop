from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views import View

import ads_module.models
from site_module import models
import product_module.models


# Create your views here.


class HomePageView(View):
    def get(self, request):
        sliders = models.Slider.objects.filter(is_active=True).all()
        site_setting: models.site_setting = models.site_setting.objects.filter(is_main_setting=True).first()
        products = product_module.models.Product.objects.filter(is_active=True).all()

        ads = ads_module.models.Ads.objects.filter(is_active=True)
        context = {
            'sliders': sliders,
            'site_setting': site_setting,
            'products': products,
            'ads': ads
        }
        return render(request, 'home_module/home_page.html', context)

    def post(self, request: HttpRequest):
        search_item = str(request.POST["search"]).lower()
        if search_item == "" or search_item is None:
            type_search_result = "str"
            context = {"result_products": "متن خالی نمیتواند یک جستجو باشد .", "search_item": search_item,
                       "type_search_result": type_search_result}
        else:
            search_in_product = product_module.models.Product.objects.filter(name__icontains=search_item).all()
            if search_in_product:
                type_search_result = "list"
                context = {"result_products": search_in_product, "search_item": search_item,
                           "type_search_result": type_search_result}
            else:
                search_in_product = product_module.models.Product.objects.filter(slug__icontains=search_item).all()
                type_search_result = "list"
                if not search_in_product:
                    search_in_product = "محصولی برای کلمه یا حرف جستجو شده شما پیدا نشد ... !"
                    type_search_result = "str"
                    print(type_search_result)
                context = {"result_products": search_in_product, "search_item": search_item,
                           "type_search_result": type_search_result}
        return render(request, "home_module/search_result.html", context)
