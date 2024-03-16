from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response

from .models import *
from rest_framework.views import APIView
from account_module.models import Comment
from .serializers import GetProductById


# Create your views here.


class ProductDetailView(View):
    def get(self, request: HttpRequest, slug):
        try:
            product = Product.objects.filter(slug__iexact=slug).first()
            about_product = AboutProduct.objects.filter(product_id=product.id).first()
            favorite_product_id = request.session.get("is_favorite")
            is_favorite = favorite_product_id == str(product.id)
            all_products = Product.objects.filter(is_active=True).all()
            comments = Comment.objects.filter(product_id=product.id, is_read_by_admin=True, parent_id=None).all()
            context = {"product": product, "about_product": about_product, "is_favorite": is_favorite,
                       "comments": comments , "all_products":all_products}

        except:
            print("error")
            context = {}

        return render(request, 'product_module/product_detail.html', context)

    def post(self):

        pass


class AddFavoriteProductView(View):
    def post(self, request: HttpRequest):
        product_id = request.POST["product_id"]
        print(product_id)
        product = Product.objects.get(pk=product_id)
        print(product.name)
        request.session["is_favorite"] = product_id
        return redirect(reverse("product_detail", args=[product.slug]))


class AddCommentView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            user_id = request.user.id
            message = request.GET.get("message")
            product_id = request.GET.get("product_id")
            parent_id = request.GET.get("parent_id")
            if parent_id is '':
                if message == "" or message is None:
                    return JsonResponse({"status": "نظر نمی تواند خالی باشد !"})
                else:
                    product = Product.objects.filter(pk=int(product_id))
                    if product.exists():
                        product = Product.objects.filter(pk=product_id).first()

                        comment = Comment.objects.create(user_id=user_id, product=product, message=message,
                                                         parent_id=None
                                                         )
                        comment.save()
                        return JsonResponse(
                            {"status": "پیام شما با موفقیت ارسال شد و پس از تایید مدیر به نمایش در خواهد آمد ."})

                    else:
                        return JsonResponse({"status": "محصول مورد نظر یافت نشد !"})
            else:
                if message == "" or message is None:
                    return JsonResponse({"status": "نظر نمی تواند خالی باشد !"})
                else:
                    product = Product.objects.filter(pk=int(product_id))
                    if product.exists():
                        product = Product.objects.filter(pk=product_id).first()

                        comment = Comment.objects.create(user_id=user_id, is_read_by_admin=True, product=product,
                                                         message=message,
                                                         parent_id=int(parent_id)
                                                         )
                        comment.save()
                        return JsonResponse(
                            {"status": "پیام شما با موفقیت ارسال شد و پس از تایید مدیر به نمایش در خواهد آمد ."})

                    else:
                        return JsonResponse({"status": "محصول مورد نظر یافت نشد !"})
        else:
            return JsonResponse({"status": "برای ارسال نظر باید به اکانت خود وارد و یا در سایت ما ثبت نام کنید."})


class AllProductView(View):
    def get(self, request: HttpRequest):
        brand_id = request.GET.get("brand_id")
        if brand_id:
            products = Product.objects.filter(is_active=True, brand_id=brand_id).all()
            for brd in products:
                print(brd)
            brands = ProductBrand.objects.all()
            context = {"products": products, "brands": brands}
        else:
            products = Product.objects.filter(is_active=True).all()
            brands = ProductBrand.objects.all()
            context = {"products": products, "brands": brands}
        return render(request, "product_module/all_product.html", context)

    def post(self):
        pass
