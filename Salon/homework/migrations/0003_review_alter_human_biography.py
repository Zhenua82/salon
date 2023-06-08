# Generated by Django 4.2.1 on 2023-06-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_alter_profession_options_profession_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, verbose_name='Текст отзыва')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='human',
            name='biography',
            field=models.TextField(blank=True, verbose_name='Специализация'),
        ),
    ]
