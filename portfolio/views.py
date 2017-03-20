from django.shortcuts import render
from .models import Product, ProductDetail, ImageFile
from django.http import Http404
# Create your views here.


def index(request):
    old_product_list = Product.objects.filter(identifier=1)[:4]
    context = {'old_product_list': old_product_list}
    return render(request, 'portfolio/index.html', context)


def engineer_work_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    if product.identifier.name == 'engineer':
        image_file_list_not_contain_S3 = ImageFile.objects.filter(product=product.pk)\
                                            .exclude(title='S3').order_by('title')
        image_file_S3 = ImageFile.objects.get(product=product.pk, title='S3')
        product_detail = ProductDetail.objects.get(product=product.pk)

        return render(request, 'portfolio/engineer_work_detail.html',
                      {'product': product, 'product_detail': product_detail,
                       'image_file_list_not_contain_S3': image_file_list_not_contain_S3,
                       'image_file_S3': image_file_S3})
    else:
        raise Http404("Product does not exist")


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
