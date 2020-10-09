from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    fields = ["event_title",
              "event_published",
              "event_content"]

admin.site.register(Event, EventAdmin)
