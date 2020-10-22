# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Checkin


class CheckinAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'contactid', 'employeeid']
    list_filter = ['timestamp', 'contactid', 'employeeid']
    search_fields = ['timestamp', 'contactid', 'employeeid']


# Register
admin.site.register(Checkin, CheckinAdmin)
