from django.db import models


class Covenant(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    ABEYANCE = 'abeyance'
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (ABEYANCE, 'Abeyance'),
    )

    title = models.CharField(max_length=100)
    doc = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    email = models.EmailField(max_length=200, null=True, blank=True, db_index=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, db_index=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
