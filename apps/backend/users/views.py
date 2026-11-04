from rest_framework import viewsets
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from .models import User, Role
from .serializers import UserSerializer, RoleSerializer


class RoleViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsTenantMember]


class UserViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsTenantMember]
