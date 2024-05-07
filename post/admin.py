from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from post.models import Cars, Category, Wheel, Transmission, CarModel, Images


@admin.register(Cars)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'user', 'wheel',
                       'transmission', 'released', 'mileage', 'color',
                       'engine', 'condition', 'category', 'car_model')
        }),
        ('Date information', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    list_display = ('title', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'text')
    ordering = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)
        return queryset


admin.site.register(Category)
admin.site.register(Wheel)
admin.site.register(Transmission)
admin.site.register(CarModel)
admin.site.register(Images)
