from django.db import models


class Metric(models.Model):
    temp = models.FloatField(
        verbose_name='Температура'
    )
    pressure = models.FloatField(
        verbose_name='Давление'
    )
    humidity = models.FloatField(
        verbose_name='Влажность'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время записили'
    )
    sensor = models.ForeighKey(
        to='Sensor',
        on_delete=models.CASCADE,
        verbose_name='Датчик',
        related_name='metrics'
    )

    def __str__(self):
        return f'Изменерения от {self.dateandtime.date()} по времени {self.dateandtime.time()} UTC'


class Location(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=256,
        blank=True,
        null=True,
    )
    parent = models.ForeighKey(
        to=self,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=256,
        blank=True,
        null=True,
    )
    serial = models.CharField(
        verbose_name='Серийный номер',
        max_length=256,
    )
    specifications = models.JsonField(
        verbose_name='Характеристики'
    )
    location = models.ForeighKey(
        to='Location',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name or self.serial
