# Generated by Django 4.1.7 on 2023-03-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoLayOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя нанесения логотипа')),
                ('image_1', models.ImageField(upload_to='logo-lay-ons/', verbose_name='Фото нанесения 1')),
                ('image_2', models.ImageField(upload_to='logo-lay-ons/', verbose_name='Фото нанесения 2')),
                ('image_3', models.ImageField(upload_to='logo-lay-ons/', verbose_name='Фото нанесения 3')),
                ('image_4', models.ImageField(upload_to='logo-lay-ons/', verbose_name='Фото нанесения 4')),
                ('video', models.CharField(max_length=500, verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Нанесение логотипа',
                'verbose_name_plural': 'Нанесения логотипа',
                'ordering': ('id',),
            },
        ),
    ]