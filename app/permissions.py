from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.roles.filter(name='Super Admin').exists()

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.roles.filter(name='Admin').exists()

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.roles.filter(name='Manager').exists()

class IsMember(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.roles.filter(name='Member').exists()

class IsSuperAdminOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and
                (request.user.roles.filter(name='Super Admin').exists() or
                 request.user.roles.filter(name='Admin').exists()))

class OrganizationPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return IsSuperAdmin().has_permission(request, view) or IsAdmin().has_permission(request, view)
        if request.method in ['PUT', 'PATCH']:
            if IsSuperAdmin().has_permission(request, view):
                return True
            if IsAdmin().has_permission(request, view):
                return view.get_object().id == request.user.organization_id
        if request.method == 'DELETE':
            if IsSuperAdmin().has_permission(request, view):
                return True
            if IsAdmin().has_permission(request, view):
                return view.get_object().id == request.user.organization_id
        return False
