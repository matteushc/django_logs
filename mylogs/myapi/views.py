from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from .serializers import LogsSerializer
from .models import Logs
from django.http import HttpResponse
import datetime
from datetime import date
import calendar
from calendar import HTMLCalendar


class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all().order_by('name_app')
    serializer_class = LogsSerializer


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)

    return render(request, 'base.html', {'title': title, 'cal': cal})

# Create your views here.
class IndexView(generic.ListView):
    model = Logs
    template_name = 'base.html'
    
    def get_queryset(self):
        return Logs.objects.all()