from rest_framework import viewsets
from .models import Organization, Role, User
from .serializers import OrganizationSerializer, RoleSerializer, UserSerializer
from .permissions import OrganizationPermission

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    # permission_classes = [OrganizationPermission]

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

