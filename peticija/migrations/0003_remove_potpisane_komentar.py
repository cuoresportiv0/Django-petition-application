# Generated by Django 2.0.2 on 2018-06-20 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peticija', '0002_peticije_broj_potpisa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='potpisane',
            name='komentar',
        ),
    ]