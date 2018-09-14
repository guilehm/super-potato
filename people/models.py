from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import cached_property


class People(models.Model):
    entity = models.ForeignKey(
        'register.Entity',
        related_name='%(class)s' + 's',
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=200, null=True, blank=True, db_index=True)
    birth_date = models.DateField(db_index=True)
    doc = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    home_phone_number = models.CharField(max_length=20, null=True, blank=True)
    cell_phone_number = models.CharField(max_length=20, null=True, blank=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_%(class)s' + 's',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False
    )
    address = models.ForeignKey(
        'register.Address',
        related_name='%(class)s' + 's',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @cached_property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @cached_property
    def phone_number(self):
        return self.cell_phone_number or self.home_phone_number

    @cached_property
    def public_id(self):
        return '{date}{id:04}'.format(
            date=self.date_added.strftime('%y%m%d'),
            id=self.id,
        )

    def __str__(self):
        return self.first_name


class Patient(People):
    HOLDER = 'holder'
    DEPENDENT = 'dependent'
    TYPE_CHOICES = (
        (HOLDER, 'Holder'),
        (DEPENDENT, 'Dependent')
    )

    AFFILIATED = 'affiliated'
    DISAFFILIATED = 'disaffiliated'
    ABEYANCE = 'abeyance'
    STATUS_CHOICES = (
        (AFFILIATED, 'Affiliated'),
        (DISAFFILIATED, 'Disaffiliated'),
        (ABEYANCE, 'Abeyance'),
    )

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, db_index=True)
    holder = models.ForeignKey(
        'people.Patient',
        related_name='dependents',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def clean(self):
        if self.type == self.DEPENDENT and not self.holder:
            raise ValidationError('Holder must be selected for dependents.')


class Professional(People):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    ON_HOLD = 'on_hold'
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (ON_HOLD, 'On hold'),
    )
    transfer_value = models.DecimalField(max_digits=8, decimal_places=2)
    registration_number = models.CharField(max_length=20, unique=True, db_index=True)
    service_phone_number = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, db_index=True)

    procedures = models.ManyToManyField(
        'attendance.Procedure',
        related_name='professionals',
    )

    @cached_property
    def phone_number(self):
        return self.service_phone_number or self.cell_phone_number or self.home_phone_number
