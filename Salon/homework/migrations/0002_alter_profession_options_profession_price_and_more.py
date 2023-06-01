# Generated by Django 4.2.1 on 2023-06-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profession',
            options={'ordering': ['id'], 'verbose_name': 'Профессия', 'verbose_name_plural': 'Профессии'},
        ),
        migrations.AddField(
            model_name='profession',
            name='price',
            field=models.TextField(blank=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='human',
            name='Last_name',
            field=models.TextField(blank=True, verbose_name='Портфолио'),
        ),
        migrations.AlterField(
            model_name='human',
            name='age',
            field=models.CharField(max_length=150, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='human',
            name='biography',
            field=models.TextField(blank=True, verbose_name='Мастер'),
        ),
    ]