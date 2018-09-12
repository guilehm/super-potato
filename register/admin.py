from django.contrib import admin

from register.models import Covenant


@admin.register(Covenant)
class CovenantAdmin(admin.ModelAdmin):
    list_display = ('title', 'doc', 'email', 'status')
    list_filter = ('status', 'date_added')
    search_fields = ('title', 'doc', 'email', 'phone_number')
