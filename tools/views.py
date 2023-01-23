from django.http import JsonResponse
from .models import Tool, Toolshed
from  .serializers import ToolSerializer


def tool_list(request):

    tools= Tool.objects.all()
    ToolSerializer(tools,many=True)
    return JsonResponse(ToolSerializer.data)