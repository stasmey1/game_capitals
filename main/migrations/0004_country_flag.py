# Generated by Django 3.2.9 on 2022-07-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220707_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag',
            field=models.ImageField(blank=True, null=True, upload_to='flag', verbose_name='Флаг'),
        ),
    ]
