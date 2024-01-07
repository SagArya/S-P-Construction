# Generated by Django 5.0 on 2023-12-23 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_sites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machineryreport',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='material_reports/'),
        ),
        migrations.AddField(
            model_name='materialreport',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='material_reports/'),
        ),
        migrations.AddField(
            model_name='materialreport',
            name='unit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='siteexpensereport',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='material_reports/'),
        ),
        migrations.AlterField(
            model_name='machineryreport',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='materialreport',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='siteexpensereport',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
