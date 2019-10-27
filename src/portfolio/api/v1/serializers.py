from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=False, allow_null=False, required=True, max_length=50)
    email = serializers.EmailField(allow_blank=False, allow_null=False, required=True, max_length=100)
    content = serializers.CharField(allow_blank=False, allow_null=False, required=True, max_length=3000)
