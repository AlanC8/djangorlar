from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from django.utils import timezone
from .models import ChallengeStatus, Challenge, Participant, CheckIn, Notification

class SoftDeletableAdminMixin:
    actions = ['soft_delete_selected', 'restore_selected']

    def get_queryset(self, request):
        return self.model.all_objects.all()

    def soft_delete_selected(self, request, queryset):
        queryset.update(is_deleted=True, deleted_at=timezone.now())
        self.message_user(request, f"Successfully soft-deleted {queryset.count()} items.")
    soft_delete_selected.short_description = "Soft delete selected items"

    def restore_selected(self, request, queryset):
        queryset.update(is_deleted=False, deleted_at=None)
        self.message_user(request, f"Successfully restored {queryset.count()} items.")
    restore_selected.short_description = "Restore selected items"


class ParticipantInline(TabularInline):
    model = Participant
    extra = 1
    fk_name = "challenge"
    inline_name = "participants"
    fields = ('user', 'current_streak', 'join_date')
    readonly_fields = ('join_date',)


@admin.register(ChallengeStatus)
class ChallengeStatusAdmin(SoftDeletableAdminMixin, ModelAdmin): 
    list_display = ('id', 'name', 'is_deleted')
    search_fields = ('name',)
    
    fieldsets = (
        (None, {'fields': ('name',)}),
        ('Soft Delete Status', {'classes': ('collapse',), 'fields': ('is_deleted', 'deleted_at')}),
    )
    readonly_fields = ('deleted_at',)


@admin.register(Challenge)
class ChallengeAdmin(SoftDeletableAdminMixin, ModelAdmin):
    list_display = ('id', 'name', 'creator', 'status', 'start_date', 'end_date', 'is_deleted')
    list_filter = ('is_deleted', 'status', 'start_date')
    search_fields = ('name', 'creator__email')
    ordering = ('-start_date',)
    inlines = [ParticipantInline]

    fieldsets = (
        ('Main Information', {
            'fields': ('name', 'description', 'creator')
        }),
        ('Timeline and Status', {
            'fields': ('status', ('start_date', 'end_date'))
        }),
        ('Soft Delete Status', {
            'classes': ('collapse',),
            'fields': ('is_deleted', 'deleted_at')
        }),
    )
    readonly_fields = ('deleted_at',)


@admin.register(Participant)
class ParticipantAdmin(SoftDeletableAdminMixin, ModelAdmin): 
    list_display = ('id', 'user', 'challenge', 'join_date', 'current_streak', 'is_deleted')
    list_filter = ('is_deleted', 'challenge',)
    search_fields = ('user__email', 'challenge__name')

    fieldsets = (
        ('Participation Details', {
            'fields': ('user', 'challenge')
        }),
        ('Progress', {
            'fields': ('current_streak', 'join_date')
        }),
        ('Soft Delete Status', {
            'classes': ('collapse',),
            'fields': ('is_deleted', 'deleted_at')
        }),
    )
    readonly_fields = ('join_date', 'deleted_at')


@admin.register(CheckIn)
class CheckInAdmin(SoftDeletableAdminMixin, ModelAdmin): 
    list_display = ('id', 'participant', 'check_in_date', 'is_deleted')
    list_filter = ('is_deleted', 'check_in_date',)
    search_fields = ('participant__user__email', 'participant__challenge__name')

    fieldsets = (
        (None, {
            'fields': ('participant', 'check_in_date', 'notes')
        }),
        ('Soft Delete Status', {
            'classes': ('collapse',),
            'fields': ('is_deleted', 'deleted_at')
        }),
    )
    readonly_fields = ('deleted_at',)


@admin.register(Notification)
class NotificationAdmin(SoftDeletableAdminMixin, ModelAdmin):
    list_display = ('id', 'user', 'message', 'is_read', 'created_at', 'is_deleted')
    list_filter = ('is_deleted', 'is_read', 'created_at')
    search_fields = ('user__email', 'message')

    fieldsets = (
        ('Notification Details', {
            'fields': ('user', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
        ('Soft Delete Status', {
            'classes': ('collapse',),
            'fields': ('is_deleted', 'deleted_at')
        }),
    )
    readonly_fields = ('created_at', 'deleted_at')