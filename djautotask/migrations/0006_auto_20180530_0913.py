# Generated by Django 2.0.5 on 2018-05-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djautotask', '0005_auto_20180529_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='actual_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='agreement_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='approved',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ticket',
            name='budget_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='closed_by',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='closed_date_utc',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='closed_flag',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ticket',
            name='customer_updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='date_resolved_utc',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='date_resplan_utc',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='date_responded_utc',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='entered_date_utc',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='has_child_ticket',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ticket',
            name='impact',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_in_sla',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ticket',
            name='last_updated_utc',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='parent_ticket_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='record_type',
            field=models.CharField(blank=True, choices=[('ServiceTicket', 'Service Ticket'), ('ProjectTicket', 'Project Ticket'), ('ProjectIssue', 'Project Issue')], db_index=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='required_date_utc',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='res_plan_mins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='resolve_mins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='resources',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='respond_mins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='severity',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='site_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='source',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='sub_type',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='sub_type_item',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='summary',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='updated_by',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]