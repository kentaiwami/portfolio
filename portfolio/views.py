# from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.urls import reverse

from .models import EngineerProduct, EngineerProductDetail, PhotographerProduct, Comment
from django.http import Http404, HttpResponseRedirect
from .forms import CommentForm

# Create your views here.


def index(request):
    engineer_product_list = EngineerProduct.objects.order_by('sort_id')[:4]
    photographer_product_list = PhotographerProduct.objects.order_by('sort_id')[:12]
    context = {'engineer_product_list': engineer_product_list, 'photographer_product_list': photographer_product_list}
    return render(request, 'portfolio/index.html', context)


def engineer_work_detail(request, e_product_id):
    try:
        engineer_product = EngineerProduct.objects.get(pk=e_product_id)
    except EngineerProduct.DoesNotExist:
        raise Http404("Product does not exist")

    engineer_product_detail = EngineerProductDetail.objects.filter(engineer_product=engineer_product.pk).first()
    comment_list = Comment.objects.filter(engineer_product=engineer_product.pk)

    form = CommentForm()
    context = {'engineer_product': engineer_product,
               'engineer_product_detail': engineer_product_detail,
               'comment_list': comment_list, 'form': form}
    return render(request, 'portfolio/engineer_work_detail.html', context)


def photographer_all(request):
    all_photographer_product_list = PhotographerProduct.objects.order_by('-sort_id')
    context = {'all_photographer_product_list': all_photographer_product_list}
    return render(request, 'portfolio/photographer_all.html', context)


def get_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            print(form['name'].value())
            print(form['comment_text'].value())
            print(form['id'].value())
            return HttpResponseRedirect(reverse('portfolio:thanks'))

    # raise ValidationError(
    #     ('Invalid value: %(value)s'),
    #     params={'value': '42'},
    # )


def thanks(request):
    return render(request, 'portfolio/thanks.html')


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
