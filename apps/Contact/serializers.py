from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'phone_number', 'whatsapp_number',
                  'instagram_account', 'telegram_account',
                  'email', 'address', 'address_url', 'business_hours')
