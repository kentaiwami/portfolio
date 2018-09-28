from rest_framework import viewsets
from .serializers import ContactSerializer
from rest_framework import serializers
from rest_framework.response import Response
from portfolio.models import Contact
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage


class ContactViewSet(viewsets.ViewSet):
    serializer_class = ContactSerializer

    @staticmethod
    def create(request):
        """
        お問い合わせを追加・メール送信する
        :param request: name, email, content
        :return:        name, email, content
        """

        data = request.data
        serializer = ContactSerializer(data=data)

        if not (serializer.is_valid() and request.method == 'POST'):
            raise serializers.ValidationError(serializer.errors)

        new_contact = Contact()
        new_contact.name = data['name']
        new_contact.email = data['email']
        new_contact.content = data['content']
        new_contact.save()

        try:
            EmailMessage(
                u'{}さんからお問い合わせがありました'.format(new_contact.name),
                u'{}'.format(new_contact.content),
                to=[EMAIL_HOST_USER]
            ).send()
        except Exception as e:
            print(e)

        return Response({'result': {
            'name':     new_contact.name,
            'email':    new_contact.email,
            'content':  new_contact.content,
        }})
