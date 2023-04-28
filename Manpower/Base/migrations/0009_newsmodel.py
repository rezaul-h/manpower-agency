# Generated by Django 4.1.7 on 2023-04-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0008_customrecruitersuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=200, null=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('newsimage', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('summary', models.TextField(blank=True, max_length=2000, null=True)),
                ('body', models.TextField(blank=True, max_length=3000, null=True)),
                ('tags', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
