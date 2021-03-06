# Generated by Django 3.0.8 on 2020-08-12 04:44

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
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathers_name', models.CharField(blank=True, max_length=80, null=True)),
                ('contact_number', models.IntegerField(null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(max_length=3, null=True)),
                ('designation', models.CharField(max_length=5, null=True)),
                ('blood_group', models.CharField(max_length=10, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='profiles/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Register',
            },
        ),
    ]
