from rest_framework import serializers

from .models import Logs

class LogsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Logs
        fields = ('name_app', 'data', 'message', 'type_message')