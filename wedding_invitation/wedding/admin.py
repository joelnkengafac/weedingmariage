from django.contrib import admin
from .models import RSVP, GuestbookEntry, GalleryPhoto


@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'attendance', 'guests', 'created_at']
    list_filter = ['attendance']
    search_fields = ['name', 'phone']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(GuestbookEntry)
class GuestbookEntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'message_preview', 'created_at']
    search_fields = ['name', 'message']
    readonly_fields = ['created_at']

    def message_preview(self, obj):
        return obj.message[:60] + '…' if len(obj.message) > 60 else obj.message
    message_preview.short_description = 'Message'


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ['caption', 'order']
    list_editable = ['order']
    ordering = ['order']
