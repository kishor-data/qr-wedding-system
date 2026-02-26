from django.contrib import admin
from django.utils.html import format_html
from .models import Event, EventImage


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'qr_preview')

    def qr_preview(self, obj):
        if obj.qr_code:
            return format_html('<img src="{}" width="100" />', obj.qr_code.url)
        return "No QR"

    qr_preview.short_description = "QR Code"


admin.site.register(Event, EventAdmin)
admin.site.register(EventImage)