# Generated by Django 4.1.7 on 2023-04-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0006_jobdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdata',
            name='company_description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]