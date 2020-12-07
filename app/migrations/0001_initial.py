# Generated by Django 2.1.15 on 2020-12-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('alpha1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alpha1')),
                ('alpha2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alpha2')),
                ('alpha3', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alpha3')),
                ('app_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='App name')),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'app_coverage',
            },
        ),
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=30)),
                ('alpha1', models.CharField(blank=True, max_length=100, verbose_name='Alpha1')),
                ('alpha2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alpha2')),
                ('alpha3', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alpha3')),
                ('app_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='App name')),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'app_execution',
            },
        ),
    ]
