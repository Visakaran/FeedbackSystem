# Generated by Django 4.2.4 on 2023-08-19 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_delete_app1_app_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='email',
            new_name='name',
        ),
    ]