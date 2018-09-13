from django.contrib import admin

from people.models import Patient, Professional


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


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'registration_number',
        'email',
        'status'
    )
    raw_id_fields = ('address', 'entity')
