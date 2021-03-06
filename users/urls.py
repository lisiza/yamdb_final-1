from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path("email/", get_confirmation_code, name="token_obtain_pair"),
    path('token/', get_jwt_token, name='token'),
]
