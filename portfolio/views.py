from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from .models import EngineerProduct, PhotographerProduct, Comment
from .forms import CommentForm


def index(request):
    engineer_product_list = EngineerProduct.objects.order_by('sort_id')
    photographer_product_list = PhotographerProduct.objects.order_by('sort_id')[:12]
    context = {'engineer_product_list': engineer_product_list, 'photographer_product_list': photographer_product_list}
    return render(request, 'portfolio/index.html', context)


def engineer_work_detail(request, e_product_id):
    try:
        engineer_product = EngineerProduct.objects.get(pk=e_product_id)
    except EngineerProduct.DoesNotExist:
        raise Http404("Product does not exist")

    comment_list = Comment.objects.filter(engineer_product=engineer_product.pk).order_by('-pub_date')

    form = CommentForm()
    context = {'engineer_product': engineer_product,
               'comment_list': comment_list, 'form': form}
    return render(request, 'portfolio/engineer_work_detail.html', context)


def all_photographer_works(request):
    all_photographer_product_list = PhotographerProduct.objects.order_by('-sort_id')
    context = {'all_photographer_product_list': all_photographer_product_list}
    return render(request, 'portfolio/all_photographer_works.html', context)


def get_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            product = EngineerProduct.objects.get(pk=form.cleaned_data['id'])
            obj = Comment()

            if form.cleaned_data['name'] != '':
                obj.name = form.cleaned_data['name']

            obj.comment_text = form.cleaned_data['comment_text']
            obj.engineer_product = product
            obj.save()

            return HttpResponseRedirect(reverse('portfolio:thanks'))

    else:
        form = CommentForm()

    engineer_product = EngineerProduct.objects.get(pk=form.cleaned_data['id'])
    context = {'form': form, 'engineer_product': engineer_product}
    return render(request, 'portfolio/form_error.html', context)


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
