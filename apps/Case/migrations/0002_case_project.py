# Generated by Django 2.1.11 on 2021-01-25 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Project', '0001_initial'),
        ('Case', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.Project'),
        ),
    ]
