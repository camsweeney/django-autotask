# Generated by Django 2.0.5 on 2018-06-01 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djautotask', '0016_auto_20180531_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='hourly_factor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='hourly_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='is_excluded_from_new_contracts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='name',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='role_type',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='system_role',
            field=models.BooleanField(default=False),
        ),
    ]