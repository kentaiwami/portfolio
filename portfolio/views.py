from django.shortcuts import render
from .models import EngineerProduct, EngineerProductDetail
from django.http import Http404
# Create your views here.


def index(request):
    product_list = EngineerProduct.objects.filter(identifier=1).order_by('sort_id')[:4]
    TEST_COUNT = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    context = {'product_list': product_list, 'TEST_COUNT': TEST_COUNT}
    return render(request, 'portfolio/index.html', context)


def engineer_work_detail(request, product_id):
    try:
        product = EngineerProduct.objects.get(pk=product_id)
    except EngineerProduct.DoesNotExist:
        raise Http404("Product does not exist")

    # if product.identifier.name == 'engineer':
    #     image_file_list_not_contain_S3 = ImageFile.objects.filter(product=product.pk)\
    #                                     .exclude(title='S3').order_by('title')
    #     image_file_S3 = ImageFile.objects.filter(product=product.pk, title='S3').first()
    product_detail = EngineerProductDetail.objects.filter(product=product.pk).first()

    context = {'product': product, 'product_detail': product_detail}
    return render(request, 'portfolio/engineer_work_detail.html', context)
    # else:
    #     raise Http404("Product does not exist")


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
