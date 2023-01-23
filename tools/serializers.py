from rest_framework import serializers
from .models import Tool
from .models import Toolshed


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toolshed
        fields= ['id','name']

    class Meta:
        model = Tool
        fields = ['name','model','type','charger']
        