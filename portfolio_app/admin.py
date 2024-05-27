from django.contrib import admin
from .models import contactmodel

class contact_form_model(admin.ModelAdmin):
    list_display = ['inserted', 'name', 'email', 'message']
admin.site.register(contactmodel, contact_form_model)
