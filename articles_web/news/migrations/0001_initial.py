# Generated by Django 4.1.5 on 2023-01-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Nazwa artykułu', max_length=50, verbose_name='Nagłówek')),
                ('anons', models.CharField(default='Jakaś część od artykułu', max_length=250, verbose_name='Wstępna część')),
                ('full_text', models.TextField(default='Jakiś text', verbose_name='Cały tekst')),
                ('date', models.DateTimeField(verbose_name='Czas tworzenia')),
            ],
            options={
                'verbose_name': 'Artykuł',
                'verbose_name_plural': 'Artykuły',
            },
        ),
    ]
