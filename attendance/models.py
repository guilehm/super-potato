from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Service(models.Model):
    health_plan = models.ForeignKey(
        'register.HealthPlan',
        related_name='services',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50, db_index=True)
    entity = models.ForeignKey(
        'register.Entity',
        related_name='services',
        on_delete=models.CASCADE,
        editable=False,
    )
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_services',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('name', 'health_plan'),)

    def save(self, *args, **kwargs):
        self.entity = self.health_plan.entity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    entity = models.ForeignKey(
        'register.Entity',
        related_name='specialties',
        on_delete=models.CASCADE,
        editable=False,
    )
    service = models.ForeignKey(
        'attendance.Service',
        related_name='specialties',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, db_index=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Specialties'
        unique_together = (('name', 'service'),)

    def save(self, *args, **kwargs):
        self.entity = self.service.health_plan.entity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Procedure(models.Model):
    entity = models.ForeignKey(
        'register.Entity',
        related_name='procedures',
        on_delete=models.CASCADE,
        editable=False,
    )
    specialty = models.ForeignKey(
        'attendance.Specialty',
        related_name='procedures',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, db_index=True)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    transfer_value = models.DecimalField(max_digits=8, decimal_places=2)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.value < self.transfer_value:
            raise ValidationError('Transfer value must not be greater than value.')

    class Meta:
        unique_together = (('name', 'specialty'),)

    def save(self, *args, **kwargs):
        self.entity = self.specialty.service.health_plan.entity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
