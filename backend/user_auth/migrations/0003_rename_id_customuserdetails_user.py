# Generated by Django 5.1.5 on 2025-01-28 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_alter_customuseraddress_second_line_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuserdetails',
            old_name='id',
            new_name='user',
        ),
    ]
