# Generated by Django 4.2.11 on 2024-06-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipify', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('ingredients', models.TextField()),
                ('method', models.TextField()),
            ],
        ),
    ]
