# Generated by Django 4.1.7 on 2023-04-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0007_alter_jobdata_company_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomRecruitersUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RecruitersName', models.CharField(max_length=100)),
                ('RecruitersUserName', models.CharField(max_length=100)),
                ('Recruitersemail', models.EmailField(max_length=254, unique=True)),
                ('Recruiterspassword', models.CharField(max_length=255)),
            ],
        ),
    ]
