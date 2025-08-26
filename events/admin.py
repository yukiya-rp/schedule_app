from django.contrib import admin
from .models import Event, User

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_time', 'end_time', 'location']
    list_filter = ['start_time', 'location']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'jersey_number', 'position', 'age']
    list_filter = ['position', 'age']
    search_fields = ['name', 'jersey_number']
    ordering = ['jersey_number']