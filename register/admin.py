from django.contrib import admin

from register.models import Entity, Covenant


@admin.register(Covenant)
class CovenantAdmin(admin.ModelAdmin):
    list_display = ('title', 'doc', 'email', 'status')
    list_filter = ('status', 'date_added')
    search_fields = ('title', 'doc', 'email', 'phone_number')


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'doc', 'entity', 'website')
    list_filter = ('entity', 'date_added')
    search_fields = ('name', 'doc', 'email', 'phone_number', 'website')
