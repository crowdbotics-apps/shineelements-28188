from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MessageViewSet, HomePageViewSet, CustomTextViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("homepage", HomePageViewSet)
router.register("message", MessageViewSet)
router.register("customtext", CustomTextViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
