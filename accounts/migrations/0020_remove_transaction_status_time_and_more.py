# Generated by Django 4.0.5 on 2022-06-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_transaction_reason_of_decline_if_any_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='status_time',
        ),
        migrations.AddField(
            model_name='transaction',
            name='Approved_or_Declined_By',
            field=models.CharField(blank=True, choices=[('CH', 'CH'), ('SA', 'SA'), ('SL', 'SL')], max_length=100),
        ),
    ]
