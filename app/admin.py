from django.contrib import admin
from .models import Organization, Role, User

@admin.register(Organization)
class OrganizationModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created_at")

@admin.register(Role)
class RoleModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "organization")  

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Role
        fields = '__all__'
