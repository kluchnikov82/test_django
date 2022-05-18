from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import PointSalseSzr, VisitSzr
from .models import *
import datetime


class ListPointSaleView(generics.ListAPIView):
    """
    Представление выводящее список торговвых точек
    """
    serializer_class = PointSalseSzr

    def get(self, request, *args, **kwargs):
        try:
            Worker.objects.get(number_phone=request.query_params['num_ph'])
        except Worker.DoesNotExist:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={'message': 'Не существует работника с таким мобильным номером'}
            )

        points_sale = PointSale.objects.filter(worker_id__number_phone=request.query_params['num_ph'])
        if not points_sale.exists():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'message': 'С данным работником не связано ни одной торговой точки'}
            )

        serializer = PointSalseSzr(points_sale, many=True)

        return Response(data={'Points of sale:': serializer.data}, status=status.HTTP_200_OK)


class VisitPoinSaleView(generics.CreateAPIView):
    """
    Представление создающее посещение торговвой точки
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSzr

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            PointSale.objects.get(uuid=data['point_sale_id'])
        except PointSale.DoesNotExist:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'message': 'Не существует торговой точки с таким ID'}
            )
        data['date_visit'] = datetime.datetime.now()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        c = serializer.save()

        return Response(
            status=status.HTTP_200_OK,
            data={'Посещение торговой точки:': serializer.data}
        )
