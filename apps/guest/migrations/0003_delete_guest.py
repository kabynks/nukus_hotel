# Generated by Django 4.2.8 on 2024-03-14 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0002_alter_guest_first_name_alter_guest_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Guest',
        ),
    ]
