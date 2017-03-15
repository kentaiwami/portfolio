from django.shortcuts import render
from .models import Product
# Create your views here.


def index(request):
    old_product_list = Product.objects.filter(identifier=1)[:6]
    context = {'old_product_list': old_product_list}
    return render(request, 'portfolio/index.html', context)
