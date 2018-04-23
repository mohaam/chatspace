# Generated by Django 2.0.4 on 2018-04-22 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masseages',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masseages', to='index.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
