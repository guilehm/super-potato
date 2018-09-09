from django.contrib import admin
from people.models import Patient, Address


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'birth_date', 'type', 'status')
    list_filter = ('status', 'type', 'date_added')
    raw_id_fields = ('holder',)
    search_fields = (
        'name',
        'email',
        'birth_date',
        'home_phone_number',
        'cell_phone_number',
        'holder',
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('patient', 'district', 'city', 'state')
    list_filter = ('city', 'state')
    search_fields = ('address', 'district')
