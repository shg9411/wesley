from django import template
import datetime
from ..models import Study

register = template.Library()


@register.filter(name='change')
def change(value):
    tmp = value.split()
    tt = datetime.time(int(tmp[0]), int(tmp[1]), 00)
    return Study.objects.filter(time=tt, teacher=int(tmp[2]), days_of_week=tmp[3]).first()
