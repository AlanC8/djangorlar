from django.contrib import admin
from .models import User

class SoftDeletableAdminMixin:
    actions = ['soft_delete_selected', 'restore_selected']

    def get_queryset(self, request):
        return self.model.all_objects.all()

    def soft_delete_selected(self, request, queryset):
        queryset.update(is_deleted=True, deleted_at=timezone.now())
        self.message_user(request, f"Succsefully 'softly' deleted {queryset.count()} objects.")
    soft_delete_selected.short_description = "Softly delete selected objects"

    def restore_selected(self, request, queryset):
        queryset.update(is_deleted=False, deleted_at=None)
        self.message_user(request, f"Succsefully restored {queryset.count()} objects.")
    restore_selected.short_description = "Restore selected objects"

@admin.register(User)
class UserAdmin(SoftDeletableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'created_at', 'is_staff', 'is_active', 'is_deleted')
    list_filter = ('is_staff', 'is_active', 'is_deleted')
    search_fields = ('email', 'username')
    ordering = ('-created_at',)
    
    fieldsets = (
        (
            ('Personal Info'), {
                'fields': ('username', 'email')
            }
        ),
        (
            ('Permissions and Statuses'), {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
            }
        ),
        (
            ('Important Dates'), {
                'fields': ('last_login', 'created_at')
            }
        ),
        (
            ('Soft Delete Status'), {
                'classes': ('collapse',),
                'fields': ('is_deleted', 'deleted_at'),
            }
        ),
    )
    
    readonly_fields = ('last_login', 'created_at', 'deleted_at')