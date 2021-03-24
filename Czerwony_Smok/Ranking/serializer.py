from .models import Fighter, Payment
from rest_framework import serializers


class FighterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fighter
        fields = ['id', 'name', 'surname', 'club']


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'fighter', 'status']
