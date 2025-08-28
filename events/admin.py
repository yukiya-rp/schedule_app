from django.contrib import admin
from .models import Event, User, Position

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_time', 'end_time', 'location', 'created_at', 'updated_at', 'is_deleted']
    list_filter = ['start_time', 'location', 'is_deleted', 'created_at']
    search_fields = ['title', 'location', 'description']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']
    
    def get_queryset(self, request):
        """論理削除されたイベントも含めて表示"""
        return Event.objects.all()
    
    def soft_delete(self, request, queryset):
        """選択されたイベントを論理削除"""
        for event in queryset:
            event.soft_delete()
        self.message_user(request, f"{queryset.count()}件のイベントを論理削除しました。")
    soft_delete.short_description = "選択されたイベントを論理削除"
    
    def restore(self, request, queryset):
        """選択されたイベントを復元"""
        for event in queryset:
            event.restore()
        self.message_user(request, f"{queryset.count()}件のイベントを復元しました。")
    restore.short_description = "選択されたイベントを復元"
    
    actions = [soft_delete, restore]

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