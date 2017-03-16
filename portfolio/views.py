from django.shortcuts import render
from .models import Product
from django.http import Http404
# Create your views here.


def index(request):
    old_product_list = Product.objects.filter(identifier=1)[:6]
    context = {'old_product_list': old_product_list}
    return render(request, 'portfolio/index.html', context)


def engineer_work_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    if product.identifier.name == 'engineer':
        return render(request, 'portfolio/engineer_work_detail.html', {'product': product})
    else:
        raise Http404("Product does not exist")


def engineer_works_all(request):
    return render(request, 'portfolio/engineer_works_all.html')
