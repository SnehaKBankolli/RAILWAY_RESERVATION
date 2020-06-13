from django.contrib import admin

# Register your models here.

from .models import Train,Ticket

admin.site.register(Train)
admin.site.register(Ticket)
