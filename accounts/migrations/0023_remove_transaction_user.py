# Generated by Django 4.0.5 on 2022-06-20 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_transaction_transaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
    ]