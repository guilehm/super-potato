from django.contrib import admin

from attendance.models import Procedure, Service, Specialty


class SpecialtyInline(admin.TabularInline):
    model = Specialty
    extra = 0


class ProcedureInline(admin.TabularInline):
    model = Procedure
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'health_plan', 'entity')
    list_filter = ('health_plan', 'entity')
    search_fields = ('name',)
    inlines = (SpecialtyInline,)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'entity')
    list_filter = ('service', 'entity')
    search_fields = ('name',)
    inlines = (ProcedureInline,)


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'transfer_value', 'specialty', 'entity')
    list_filter = ('specialty', 'entity')
    search_fields = ('name',)
