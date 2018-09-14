from django.contrib import admin

from people.models import Patient, Professional


class ProcedureInline(admin.TabularInline):
    model = Professional.procedures.through
    extra = 0


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'birth_date', 'type', 'status')
    list_filter = ('status', 'type', 'date_added')
    raw_id_fields = ('holder', 'address', 'entity')
    readonly_fields = ('public_id',)
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'birth_date',
        'home_phone_number',
        'cell_phone_number',
        'holder',
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.added_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'registration_number',
        'email',
        'status'
    )
    exclude = ('procedures',)
    inlines = (ProcedureInline,)
    raw_id_fields = ('address', 'entity')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.added_by = request.user
        super().save_model(request, obj, form, change)
