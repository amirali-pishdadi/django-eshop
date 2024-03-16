import datetime
import time
import requests
import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse
from django.http import HttpRequest, JsonResponse
from .models import *

# if settings.SANDBOX:
#     sandbox = 'sandbox'
# else:
#     sandbox = 'www'

sandbox = 'sandbox'
MERCHANT = "YOUR_MERCHANT"
ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

description = "خرید از فروشگاه من"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/order/verify-payment/'


# Create your views here.
class UserBaskedView(View):
    def get(self, request: HttpRequest):
        current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
        order_detail = current_order.orderdetail_set.all()
        mablagh_pardakht = 0
        kol_pardakht = 0
        moblagh_after_discount = 0
        for order in order_detail:
            mablagh_pardakht += order.dicount()
            kol_pardakht += order.jam()
            moblagh_after_discount += order.dicount_mablagh_pardakht()
        context = {
            "order_detail": order_detail,
            "mablagh_discount": int(mablagh_pardakht),
            "kol_pardakht": kol_pardakht,
            "after_discount": int(moblagh_after_discount)
        }
        return render(request, "order_module/order_page.html", context)

    def post(self, request: HttpRequest):
        pass


class AddProductView(View):
    def get(self, request: HttpRequest):
        count = request.GET.get("count")
        product_id = request.GET.get("product_id")
        if int(count) < 0:
            print("- count")
            return JsonResponse({
                "text": "تعداد منفی نمیشود",
                "icon": "warning",
                "confirm": "آها !"
            })
        else:
            print(count, product_id)
        if request.user.is_authenticated:
            product = Product.objects.filter(pk=product_id)
            if product.exists():
                current_order, created = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
                current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
                try:
                    if current_order_detail.count > product.first().quantity:
                        current_order_detail.count = product.first().quantity
                        current_order_detail.save()
                        return JsonResponse({
                            "text": "موجودی محصول کافی نیست",
                            "icon": "warning",
                            "confirm": "باشه"
                        })
                except:
                    pass
                if current_order_detail is not None:
                    current_order_detail.count += int(count)
                    current_order_detail.save()
                    return JsonResponse({
                        "text": "محصول با موفقیت به سبد خرید شما افزوده شد",
                        "icon": "success",
                        "confirm": "باشه"
                    })
                else:
                    new_detail = OrderDetail.objects.create(order=current_order, product_id=product_id,
                                                            count=count)
                    new_detail.save()
                    return JsonResponse({
                        "text": "محصول با موفقیت به سبد خرید شما افزوده شد",
                        "icon": "success",
                        "confirm": "باشه"
                    })
            else:
                return JsonResponse({
                    "text": "محصول مورد نظر وجود ندارد",
                    "icon": "warning",
                    "confirm": "باشه"
                })
        else:
            return JsonResponse({
                "text": "برای افزودن به سبد خرید شما باید وارد اکانت خود شوید",
                "icon": "warning",
                "confirm": "باشه"
            })

    def post(self, request: HttpRequest):
        pass


class RemoveProductView(View):
    def get(self, request: HttpRequest):
        product_id = request.GET.get("product_id")
        product = Product.objects.filter(pk=product_id)
        if request.user.is_authenticated:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail.count <= 0:
                current_order_detail.delete()
                return JsonResponse({
                    "text": "محصول مورد نظر از سبد خرید حذف شد .",
                    "icon": "success",
                    "confirm": "باشه"
                })
            else:
                if current_order_detail.count > product.first().quantity:
                    current_order_detail.count = product.first().quantity
                    current_order_detail.save()
                    return JsonResponse({
                        "text": "از تعداد محصول مورد نظر 1 واحد کسر شد .",
                        "icon": "success",
                        "confirm": "باشه"
                    })
                else:
                    current_order_detail.count = current_order_detail.count - 1
                    current_order_detail.save()
                    return JsonResponse({
                        "text": "از تعداد محصول مورد نظر 1 واحد کسر شد .",
                        "icon": "success",
                        "confirm": "باشه"
                    })
        else:
            return JsonResponse({
                "text": "برای حذف محصول از سبد خرید باید وارد اکانت خود شوید .",
                "icon": "warning",
                "confirm": "باشه"
            })

    def post(self, request: HttpRequest):
        pass


@login_required
def request_payment(request:HttpRequest):
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    order_detail = current_order.orderdetail_set.all()
    final_price = 0
    for order in order_detail:
        final_price += order.dicount_mablagh_pardakht()
    if final_price == 0:
        return redirect(reverse('user_basked'))
    data = {
        "MerchantID": MERCHANT,
        "Amount": float(final_price),
        "Description": description,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return redirect(ZP_API_STARTPAY + str(response['Authority']))
            else:
                return JsonResponse({'status': False, 'code': str(response['Status'])})
        return JsonResponse(response)

    except requests.exceptions.Timeout:
        return JsonResponse({'status': False, 'code': 'timeout'})
    except requests.exceptions.ConnectionError:
        return JsonResponse({'status': False, 'code': 'connection error'})

@login_required
def verify_payment(request: HttpRequest):
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    order_detail = current_order.orderdetail_set.all()
    t_authority = request.GET['Authority']
    final_price = 0
    for order in order_detail:
        final_price += order.dicount_mablagh_pardakht()
    data = {
        "MerchantID": MERCHANT,
        "Amount": float(final_price),
        "Authority": t_authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:

            for product_order in order_detail:
                product_id = product_order.product.id
                product = Product.objects.filter(pk=product_id , is_active=True).first()
                product.quantity = product.quantity - product_order.count
                product.save()

            current_order.is_paid = True
            current_order.payment_date = str(datetime.today().date())
            current_order.save()
            context = {'status': True, 'RefID': response['RefID']}
            return render(request , "order_module/verify_payment_ok.html" , context)
        else:
            context = {'status': False, 'RefID': response['RefID']}
            return render(request , "order_module/verify_payment_ok.html" , context)
    return JsonResponse(response)
