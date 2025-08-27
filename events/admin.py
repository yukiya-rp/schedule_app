from django.contrib import admin
from .models import Event, User, Position

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_time', 'end_time', 'location']
    list_filter = ['start_time', 'location']

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['code']
    search_fields = ['code']
    ordering = ['code']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'jersey_number', 'get_positions_display', 'age']
    list_filter = ['positions', 'age']
    search_fields = ['name', 'jersey_number']
    ordering = ['jersey_number']
    filter_horizontal = ['positions']
    
    def get_positions_display(self, obj):
        return obj.get_positions_display()
    get_positions_display.short_description = 'ポジション'