from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(conductor)
admin.site.register(ruta)
admin.site.register(empresa)
admin.site.register(Avatar)
admin.site.register(Comment)

