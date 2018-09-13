from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import cached_property


class People(models.Model):
    registration = models.CharField(max_length=11, db_index=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=200, null=True, blank=True, db_index=True)
    birth_date = models.DateField(db_index=True)
    doc = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    home_phone_number = models.CharField(max_length=20, null=True, blank=True)
    cell_phone_number = models.CharField(max_length=20, null=True, blank=True)
    # TODO: created_by
    # TODO: link to entity

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    address = models.ForeignKey(
        'register.Address',
        related_name='%(class)s' + 's',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    @cached_property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @cached_property
    def phone_number(self):
        return self.cell_phone_number or self.home_phone_number

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
