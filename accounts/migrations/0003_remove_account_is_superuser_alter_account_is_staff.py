# Generated by Django 5.0.7 on 2024-08-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_is_superadmin_account_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_superuser',
        ),
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]