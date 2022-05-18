from django.utils import timezone

from django.db import models
import uuid


class Worker(models.Model):
    """
    Модель работник
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255,
                            verbose_name='Имя работника',
                            blank=False)
    number_phone = models.CharField(max_length=255,
                            verbose_name='Номер телефона работника',
                            blank=False)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        db_table = 'worker_db'

    def __str__(self):
        return self.name


class PointSale(models.Model):
    """
    Модель торговая точка
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255,
                            verbose_name='Название торговой точки',
                            blank=False)
    worker_id = models.ForeignKey(Worker, on_delete=models.DO_NOTHING, null=True, default=None)

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'
        db_table = 'point_sale_db'

    def __str__(self):
        return '%s -> %s' % (self.name, self.uuid)

class Visit(models.Model):
    """
    Модель посещение
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    point_sale_id = models.ForeignKey(PointSale, on_delete=models.DO_NOTHING, null=True, default=None)
    date_visit = models.DateTimeField(null=True, default=None, verbose_name='Дата и время визита')
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Визит'
        verbose_name_plural = 'Визиты'
        db_table = 'visit_db'

    def __str__(self):
        return str(self.uuid)


