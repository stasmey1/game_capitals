# Generated by Django 3.2.9 on 2022-07-07 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_country_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(max_length=100, unique=True, verbose_name='Столица'),
        ),
        migrations.AlterField(
            model_name='country',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countries', to='main.group', verbose_name='Группа стран'),
        ),
        migrations.AlterField(
            model_name='country',
            name='info',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='country',
            name='сontinent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countries', to='main.continent', verbose_name='Континент'),
        ),
    ]