from django.contrib import admin
from .models import Profile, Message

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'location')
    search_fields = ('user__username', 'name', 'location')
    list_filter = ('created',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'is_read', 'created')
    search_fields = ('sender__user__username', 'recipient__user__username', 'subject')
    list_filter = ('is_read', 'created')
