# clase donde se registran las clases para el admin panel
from django.contrib import admin
from .models import user
from .models import order
from .models import client

# Register your models here.

admin.site.register(user)
admin.site.register(order)
admin.site.register(client)