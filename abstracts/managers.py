from django.db import models
from django.utils import timezone

class SoftDeletableManager(models.Manager):
    """
    Custom manager for SoftDeletableModel.
    Provides methods to handle soft-deleted objects.
    """
    def get_queryset(self):
        """
        By default, return only objects that are not soft-deleted.
        """
        return super().get_queryset().filter(is_deleted=False)

    def all_with_deleted(self):
        """
        Return all objects, including soft-deleted ones.
        """
        return super().get_queryset()

    def only_deleted(self):
        """
        Return only the soft-deleted objects.
        """
        return super().get_queryset().filter(is_deleted=True)
    
    def soft_delete(self):
        """
        Soft delete the objects in the queryset.
        """
        return self.update(is_deleted=True, deleted_at=timezone.now())