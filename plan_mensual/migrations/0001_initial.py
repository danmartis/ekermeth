# Generated by Django 2.0.4 on 2018-09-10 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto_general',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan_mensual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sueldo', models.CharField(blank=True, max_length=100, null=True)),
                ('diario', models.CharField(blank=True, max_length=100, null=True)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('total', models.CharField(blank=True, max_length=100, null=True)),
                ('gasto_general', models.ManyToManyField(blank=True, to='plan_mensual.Gasto_general')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
