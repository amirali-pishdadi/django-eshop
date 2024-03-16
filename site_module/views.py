from django.shortcuts import render
from order_module.models import Order
from account_module.models import User
from site_module import models


# Create your views here.


def site_header(request):
    site_setting = models.site_setting.objects.filter(is_main_setting=True).first()
    header_link = models.HeaderLink.objects.all()
    user = ""
    if request.user.is_authenticated:
        user_check = User.objects.filter(pk=request.user.id).first()
        if user_check.is_superuser:
            user = user_check
        current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
        order_detail = current_order.orderdetail_set.all()
        context = {
            'site_setting': site_setting,
            'header_link': header_link,
            'request': request, "user": user,
            "order_detail": order_detail,
        }
    else:
        context = {
            'site_setting': site_setting,
            'header_link': header_link,
            'request': request,
        }

    return render(request, 'header_html.html', context)


def site_footer(request):
    site_setting = models.site_setting.objects.filter(is_main_setting=True).first()
    footer_boxes = models.FooterLinkBoxes.objects.all()
    footer_links = models.FooterLink.objects.all()
    context = {
        'site_setting': site_setting,
        'footer_boxes': footer_boxes,
        'footer_links': footer_links,
    }
    return render(request, 'footer_html.html', context)
