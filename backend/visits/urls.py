from django.urls import include, path
import visits.views as views

urlpatterns = []

urlpatterns += [
    path('list_point_sale/', views.ListPointSaleView.as_view(), name='list-point-sale'),
    path('visit_point_sale/', views.VisitPoinSaleView.as_view(), name='visit-point-sale'),
]
