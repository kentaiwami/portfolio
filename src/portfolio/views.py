from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import EngineerProduct, PhotographerProduct, Comment, PrivacyPolicy, Contact
from .forms import CommentForm, ContactForm
from django.core.mail import EmailMessage
from mysite.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.messages import get_messages
from django.db import connections
from django.db.utils import OperationalError


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
    policies = PrivacyPolicy.objects.filter(engineer_product=engineer_product.pk).order_by('sort_id')
    context = {'engineer_product': engineer_product,
               'comment_list': comment_list,
               'form': CommentForm(),
               'policies': len(policies)
               }
    return render(request, 'portfolio/engineer_work_detail.html', context)


def all_photographer_works(request):
    all_photographer_product_list = PhotographerProduct.objects.order_by('-sort_id')
    context = {'all_photographer_product_list': all_photographer_product_list}
    return render(request, 'portfolio/all_photographer_works.html', context)


def post_comment(request):
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
    return render(request, 'portfolio/comment_form_error.html', context)


def post_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = Contact()
            new_contact.name = form.cleaned_data['name']
            new_contact.email = form.cleaned_data['email']
            new_contact.content = form.cleaned_data['content']
            new_contact.save()

            try:
                EmailMessage(
                    u'{}さんからお問い合わせがありました'.format(new_contact.name),
                    u'{}'.format(new_contact.content),
                    to=[EMAIL_HOST_USER]
                ).send()
            except Exception as e:
                print(e)

            messages.add_message(request, messages.SUCCESS, 'Thanks for your contact.')
            return redirect('portfolio:thanks')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact_form_error.html', {'form': form})


def contact(request):
    form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})


def thanks(request):
    storage = get_messages(request)
    msg = ''
    for message in storage:
        msg = message

    messages.add_message(request, messages.SUCCESS, msg)
    return render(request, 'portfolio/thanks.html', {'message': msg})


def privacy_policy(request, e_product_id):
    try:
        engineer_product = EngineerProduct.objects.get(pk=e_product_id)
    except EngineerProduct.DoesNotExist:
        raise Http404('Product does not exist')

    policies = PrivacyPolicy.objects.filter(engineer_product=engineer_product.pk).order_by('sort_id')

    if len(policies) == 0:
        raise Http404('Privacy Policy does not exist')

    context = {'engineer_product': engineer_product, 'policy_list': policies, 'latest': max(policies.values_list('updated_at'))[0]}
    return render(request, 'portfolio/privacy_policy.html', context)


def engineer_works_all(request):
    return render(request, 'portfolio/engineer_works_all.html')


def health_check(request):
    try:
        connections['default'].cursor()
    except OperationalError:
        return HttpResponse(status=500)

    return HttpResponse(status=200)
