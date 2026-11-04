from rest_framework import viewsets


class TenantMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        tenant = getattr(self.request, 'tenant', None) or getattr(self.request.user, 'tenant', None)
        if tenant:
            if hasattr(queryset.model, 'tenant'):
                return queryset.filter(tenant=tenant)
        return queryset

    def perform_create(self, serializer):
        tenant = getattr(self.request, 'tenant', None) or getattr(self.request.user, 'tenant', None)
        if tenant and hasattr(serializer.Meta.model, 'tenant'):
            serializer.save(tenant=tenant)
        else:
            serializer.save()


class BranchScopedMixin(TenantMixin):
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if hasattr(user, 'branch_id') and user.branch_id and hasattr(queryset.model, 'branch'):
            return queryset.filter(branch_id=user.branch_id)
        return queryset
