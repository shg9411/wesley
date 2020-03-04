from django import template
from django.shortcuts import get_object_or_404
import datetime
from ..models import Regular, Temporary

register = template.Library()


@register.filter(name='change')
def change(value):
    tmp = value.split()
    tt = datetime.time(int(tmp[0]), int(tmp[1]), 00)
    return Regular.objects.filter(time=tt, teacher=int(tmp[2]), days_of_week=tmp[3]).first()


@register.filter(name='temp')
def temp(value):
    tmp = value.split()
    tt = datetime.time(int(tmp[0]), int(tmp[1]), 00)
    temp = [t for t in Temporary.objects.filter(time=tt, teacher=int(tmp[2]), temp_date__week=datetime.date.today().isocalendar()[1]) if t.wd == int(tmp[3])]
    return temp[0] if temp else None
