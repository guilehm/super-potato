from django.db import models


class Entity(models.Model):
    NATURAL_PERSON = 'natural person'
    LEGAL_PERSON = 'legal person'
    ENTITY_TYPE = (
        (NATURAL_PERSON, 'Natural person'),
        (LEGAL_PERSON, 'Legal person'),
    )

    entity = models.CharField(max_length=20, choices=ENTITY_TYPE, db_index=True)
    name = models.CharField(max_length=50)
    doc = models.CharField(max_length=20, unique=True, db_index=True, null=True, blank=True)
    email = models.EmailField(max_length=200, db_index=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    website = models.CharField(max_length=100, unique=True, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class HealthPlan(models.Model):
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
