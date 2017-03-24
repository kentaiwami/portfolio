from django.shortcuts import render
from .models import EngineerProduct, EngineerProductDetail, PhotographerProduct
from django.http import Http404
# Create your views here.


def index(request):
    engineer_product_list = EngineerProduct.objects.order_by('sort_id')[:4]
    photographer_product_list = PhotographerProduct.objects.all()
    context = {'engineer_product_list': engineer_product_list, 'photographer_product_list': photographer_product_list}
    return render(request, 'portfolio/index.html', context)


def engineer_work_detail(request, product_id):
    try:
        engineer_product = EngineerProduct.objects.get(pk=product_id)
    except EngineerProduct.DoesNotExist:
        raise Http404("Product does not exist")

    engineer_product_detail = EngineerProductDetail.objects.filter(engineer_product=engineer_product.pk).first()

    context = {'engineer_product': engineer_product, 'engineer_product_detail': engineer_product_detail}
    return render(request, 'portfolio/engineer_work_detail.html', context)


def engineer_works_all(request):
    return render(request, 'portfolio/engineer_works_all.html')


def handler404(request):
    return render(request, 'portfolio/404.html')


def handler500(request):
    return render(request, 'portfolio/500.html')


def handler403(request):
    return render(request, 'portfolio/403.html')


def handler400(request):
    return render(request, 'portfolio/400.html')
