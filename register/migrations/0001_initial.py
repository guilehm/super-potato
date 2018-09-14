# Generated by Django 2.1.1 on 2018-09-14 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(db_index=True, max_length=10)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('complement', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(choices=[('natural person', 'Natural person'), ('legal person', 'Legal person')], db_index=True, max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('doc', models.CharField(blank=True, db_index=True, max_length=20, null=True, unique=True)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entities', to='register.Address')),
            ],
            options={
                'verbose_name_plural': 'Entities',
            },
        ),
        migrations.CreateModel(
            name='HealthPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('doc', models.CharField(blank=True, db_index=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('abeyance', 'Abeyance')], db_index=True, max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_plans', to='register.Entity')),
            ],
        ),
    ]
