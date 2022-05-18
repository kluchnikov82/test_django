from rest_framework import serializers
from .models import *


class PointSalseSzr(serializers.ModelSerializer):
    """
        Сериализатор списка торговых точек
    """
    class Meta:
        model = PointSale
        fields = (
            'uuid',
            'name'
        )


class VisitSzr(serializers.ModelSerializer):
    """
        Сериализатор модели визиты
    """

    def create(self, validated_data):
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')
        point_sale_id = validated_data.pop('point_sale_id')
        date_visit = validated_data.pop('date_visit')
        c = Visit.objects.create(
            point_sale_id=point_sale_id,
            date_visit=date_visit,
            latitude=latitude,
            longitude=longitude
        )

        return c

    class Meta:
        model = Visit
        fields = (
            'point_sale_id',
            'date_visit',
            'latitude',
            'longitude'
        )
