# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, RoleViewSet, UserViewSet

router = DefaultRouter()
router.register(r'organization', OrganizationViewSet)
router.register(r'role', RoleViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
