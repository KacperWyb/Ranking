from .models import Fighter, Payment
from rest_framework import viewsets
from .serializer import FighterSerializer, PaymentSerializer


class FighterViewSet(viewsets.ModelViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

