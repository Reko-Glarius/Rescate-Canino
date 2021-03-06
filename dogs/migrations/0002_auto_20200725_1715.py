# Generated by Django 3.1b1 on 2020-07-25 21:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dog',
            options={'ordering': ['-date'], 'verbose_name': 'Perro', 'verbose_name_plural': 'Perros'},
        ),
        migrations.AddField(
            model_name='dog',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de Registro'),
            preserve_default=False,
        ),
    ]
