from django.contrib import admin

from . import models

class MessageAdmin(admin.ModelAdmin):

    list_display = ['pk', 'message']
    list_editable = ['message']

admin.site.register(models.Message, MessageAdmin)