# Generated by Django 4.2.4 on 2023-10-08 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refferals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refferal',
            old_name='code',
            new_name='refferal_code',
        ),
    ]