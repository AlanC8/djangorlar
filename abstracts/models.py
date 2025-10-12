from django.db import models
from django.utils import timezone
from .managers import SoftDeletableManager

class AbstractSoftDeletableModel(models.Model):
    """
    An abstract model that provides soft-deletion functionality.
    """
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeletableManager()  
    all_objects = models.Manager() 

    def delete(self, using=None, keep_parents=False):
        """
        Override the default delete method to perform a soft delete.
        """
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """
        Restore a soft-deleted object.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    def hard_delete(self, using=None, keep_parents=False):
        """
        Permanently delete the object from the database.
        """
        return super().delete(using, keep_parents)

    class Meta:
        abstract = True