from rest_framework import permissions


class IsTenantMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and getattr(request.user, 'tenant_id', None))


class IsBranchUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and getattr(user, 'tenant_id', None))


class HasRolePermission(permissions.BasePermission):
    required_permission = None

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if getattr(user, 'is_superuser', False):
            return True
        role = getattr(user, 'role', None)
        if not role:
            return False
        perms = role.permissions or {}
        if self.required_permission:
            return perms.get(self.required_permission, False)
        return True


class TenantScopedPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if getattr(user, 'is_superuser', False):
            return True
        tenant_id = getattr(user, 'tenant_id', None)
        obj_tenant_id = getattr(obj, 'tenant_id', None) or getattr(getattr(obj, 'tenant', None), 'id', None)
        return tenant_id and obj_tenant_id and tenant_id == obj_tenant_id
