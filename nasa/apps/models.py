from django.db import models


class Coordinates(models.Model):
    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'

    name = models.CharField(
        verbose_name='Название спутника',
        max_length=512,
    )
    satelliteId = models.IntegerField(
        verbose_name='ID спутника',
    )
    line1 = models.CharField(
        verbose_name='Первая координата',
    )
    line2 = models.CharField(
        verbose_name='Вторая координата',
    )
    date = models.DateTimeField(
        verbose_name='Дата',
    )
