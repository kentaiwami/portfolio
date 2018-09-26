from django.shortcuts import render, redirect
from django.http import Http404
from .models import EngineerProduct, PhotographerProduct, Comment, PrivacyPolicy
from .forms import CommentForm
from django.core.mail import EmailMessage
from mysite.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.messages import get_messages


def index(request):
    engineer_product_list = EngineerProduct.objects.order_by('sort_id')
    photographer_product_list = PhotographerProduct.objects.order_by('sort_id')[:12]
    context = {'engineer_product_list': engineer_product_list, 'photographer_product_list': photographer_product_list}
    return render(request, 'portfolio/index.html', context)


def engineer_work_detail(request, e_product_id):
    try:
        engineer_product = EngineerProduct.objects.get(pk=e_product_id)
    except EngineerProduct.DoesNotExist:
        raise Http404('Product does not exist')

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
            comment = Comment()

            if form.cleaned_data['name'] != '':
                comment.name = form.cleaned_data['name']

            comment.text = form.cleaned_data['text']
            comment.engineer_product = product
            comment.save()

            try:
                EmailMessage(
                    u'{}さんが{}にコメントを追加しました'.format(comment.name, comment.engineer_product.name),
                    u'{}'.format(comment.text),
                    to=[EMAIL_HOST_USER]
                ).send()
            except Exception as e:
                print(e)

            messages.add_message(request, messages.SUCCESS, 'Thanks for your comment.')
            return redirect('portfolio:thanks')
    else:
        form = CommentForm()

    engineer_product = EngineerProduct.objects.get(pk=form.cleaned_data['id'])
    context = {'form': form, 'engineer_product': engineer_product}
    return render(request, 'portfolio/form_error.html', context)


def thanks(request):
    storage = get_messages(request)
    for message in storage:
        messages.add_message(request, messages.SUCCESS, message)
        return render(request, 'portfolio/thanks.html', {'message': message})


def privacy_policy(request, e_product_id):
    try:
        engineer_product = EngineerProduct.objects.get(pk=e_product_id)
    except EngineerProduct.DoesNotExist:
        raise Http404('Product does not exist')

    policies = PrivacyPolicy.objects.filter(engineer_product=engineer_product.pk).order_by('sort_id')

    if len(policies) == 0:
        raise Http404('Privacy Policy does not exist')

    context = {'engineer_product': engineer_product, 'policy_list': policies}
    return render(request, 'portfolio/privacy_policy.html', context)


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
