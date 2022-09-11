from .models import (
    Client
)
from django_filters import (
    rest_framework as filters
)


class ClientFilterSet(filters.FilterSet):
    """Date filters"""
    date_visit__day = filters.NumberFilter(field_name="date_visit", lookup_expr="day")
    date_visit__day__gt = filters.NumberFilter(field_name="date_visit", lookup_expr="day__gt")
    date_visit__day__lt = filters.NumberFilter(field_name="date_visit", lookup_expr="day__lt")
    date_visit__month = filters.NumberFilter(field_name="date_visit", lookup_expr="month")
    date_visit__month__gt = filters.NumberFilter(field_name="date_visit", lookup_expr="month__gt")
    date_visit__month__lt = filters.NumberFilter(field_name="date_visit", lookup_expr="month__lt")
    date_visit__year = filters.NumberFilter(field_name="date_visit", lookup_expr="year")
    date_visit__year__gt = filters.NumberFilter(field_name="date_visit", lookup_expr="year__gt")
    date_visit__year__lt = filters.NumberFilter(field_name="date_visit", lookup_expr="year__lt")
    date_joining__day = filters.NumberFilter(field_name="date_joining", lookup_expr="day")
    date_joining__day__gt = filters.NumberFilter(field_name="date_joining", lookup_expr="day__gt")
    date_joining__day__lt = filters.NumberFilter(field_name="date_joining", lookup_expr="day__lt")
    date_joining__month = filters.NumberFilter(field_name="date_joining", lookup_expr="month")
    date_joining__month__gt = filters.NumberFilter(field_name="date_joining", lookup_expr="month__gt")
    date_joining__month__lt = filters.NumberFilter(field_name="date_joining", lookup_expr="month__lt")
    date_joining__year = filters.NumberFilter(field_name="date_joining", lookup_expr="year")
    date_joining__year__gt = filters.NumberFilter(field_name="date_joining", lookup_expr="year__gt")
    date_joining__year__lt = filters.NumberFilter(field_name="date_joining", lookup_expr="year__lt")

    class Meta:
        model = Client
        fields = ("date_visit", "date_joining", "status", "active")
        
