from django.core.exceptions import ValidationError
from django.db import models


class Patient(models.Model):
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

    registration = models.CharField(max_length=11, db_index=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=200, null=True, blank=True, db_index=True)
    birth_date = models.DateField(db_index=True)
    doc = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    home_phone_number = models.CharField(max_length=20, null=True, blank=True)
    cell_phone_number = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, db_index=True)
    holder = models.ForeignKey(
        'people.Patient',
        related_name='dependents',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.type == self.DEPENDENT and not self.holder:
            raise ValidationError('Holder must be selected for dependents.')

    def __str__(self):
        return self.name


class Address(models.Model):
    patient = models.OneToOneField('people.Patient', related_name='address', on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10, db_index=True, null=True, blank=True)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=10, null=True, blank=True)
    complement = models.CharField(max_length=20, null=True, blank=True)
    district = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address
