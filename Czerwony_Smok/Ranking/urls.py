from rest_framework import routers
from django.urls import include, path
from .views import FighterViewSet, PaymentViewSet

router = routers.DefaultRouter()
router.register(r'fighters', FighterViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
