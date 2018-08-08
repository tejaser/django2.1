from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_filter = ['age', 'salary']
    list_display = ['first_name', 'last_name', 'age', 'salary']
    search_fields = ['first_name', 'last_name', 'age']


# Register your models here.
admin.site.register(Client, ClientAdmin)
