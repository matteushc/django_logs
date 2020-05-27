from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from .serializers import LogsSerializer
from .models import Logs
from django.http import HttpResponse
import datetime
import calendar
from calendar import HTMLCalendar
import requests

URL_SOLR = ""


class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all().order_by('name_app')
    serializer_class = LogsSerializer


class IndexView(generic.ListView):
    model = Logs
    template_name = 'base.html'
  
    def get_queryset(self):
        return Logs.objects.all()

class LogsView(generic.TemplateView):

    def get(self,request):
        data_atual = datetime.datetime.now()
        data_atual = data_atual.strftime("%Y-%m-%d")
        url = f'{URL_SOLR}/select?q=date:"{data_atual}"&wt=json&indent=true'
        r = requests.get(url)
        logs = r.json()
        logs_list = {'logs_list': logs['response']['docs']}
        return render(request,'buscar.html',logs_list)


def your_view(request):

    if request.method == 'GET':

        search_box = request.GET.get('search_box', None)
        data_box = request.GET.get('data_box', None)
        if search_box:
            url = f'{URL_SOLR}/select?q=name:"{search_box}"&wt=json&indent=true'
        elif data_box:
            url = f'{URL_SOLR}/select?q=date:"{data_box}"&wt=json&indent=true'
        else:
            url = f"{URL_SOLR}/select?q=*:*&wt=json&indent=true&sort=asctime desc"
        r = requests.get(url)
        logs = r.json()
        logs_list = {'logs_list': logs['response']['docs']}
        return render(request,'buscar.html',logs_list)