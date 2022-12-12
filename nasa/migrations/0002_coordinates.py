# Generated by Django 3.2.16 on 2022-11-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nasa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Название спутника')),
                ('satelliteId', models.IntegerField(verbose_name='ID спутника')),
                ('line1', models.CharField(max_length=512, verbose_name='Первая координата')),
                ('line2', models.CharField(max_length=512, verbose_name='Вторая координата')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
    ]