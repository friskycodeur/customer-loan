from .custom_claims import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.urls import path, include
from .views import (
    RegisterAPIView,
    UserDetail,
    login,
)
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterAPIView.as_view()),
    path("token/obtain/", CustomTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("users/<username>", UserDetail.as_view()),
    path("login/", login),
]
