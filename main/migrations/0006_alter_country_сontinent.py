# Generated by Django 3.2.9 on 2022-07-07 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220707_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='сontinent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countries', to='main.continent', verbose_name='Континент'),
        ),
    ]
