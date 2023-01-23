from django.contrib import admin


from .models import Tool
from .models import Toolshed
admin.site.register(Tool)
admin.site.register(Toolshed)
