# Generated by Django 2.1.1 on 2018-09-14 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0003_auto_20180914_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='added_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_services', to=settings.AUTH_USER_MODEL),
        ),
    ]
