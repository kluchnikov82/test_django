from django.contrib import admin
from .models import *


class WorkerAdmin(admin.ModelAdmin):
    fields = ('uuid' ,'name', 'number_phone')
    readonly_fields = ('uuid',)
    search_fields = ['name']

class PointSaleAdmin(admin.ModelAdmin):
    fields = ('uuid', 'name', 'worker_id')
    readonly_fields = ('uuid',)
    search_fields = ['name']

class VisitAdmin(admin.ModelAdmin):
    fields = ('uuid', 'date_visit', 'point_sale_id', 'latitude', 'longitude')
    readonly_fields = ('uuid',)
    search_fields = ['point_sale_id__name']
    search_fields = ['point_sale_id__worker_id__name']


admin.site.register(Worker, WorkerAdmin)
admin.site.register(PointSale, PointSaleAdmin)
admin.site.register(Visit, VisitAdmin)

