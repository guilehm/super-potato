from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from register.models import Address, Entity, HealthPlan, User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'entity')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'entity', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    list_filter = ('entity', 'is_staff', 'is_superuser', 'is_active')


@admin.register(HealthPlan)
class HealthPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'doc', 'email', 'status')
    list_filter = ('status', 'date_added')
    search_fields = ('name', 'doc', 'email', 'phone_number')


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'doc', 'entity', 'website')
    list_filter = ('entity', 'date_added')
    search_fields = ('name', 'doc', 'email', 'phone_number', 'website')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'district', 'city', 'state')
    list_filter = ('city', 'state')
    search_fields = ('address', 'district')
