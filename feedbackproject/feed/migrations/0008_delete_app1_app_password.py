# Generated by Django 4.2.4 on 2023-08-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_app1_remove_app_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='App1',
        ),
        migrations.AddField(
            model_name='app',
            name='password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
