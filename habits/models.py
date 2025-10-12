from django.db import models
from django.conf import settings
from abstracts.models import AbstractSoftDeletableModel

class ChallengeStatus(AbstractSoftDeletableModel):
    name = models.CharField(max_length=50, unique=True)
    class Meta: verbose_name, verbose_name_plural = "Challenge Status", "Challenge Statuses"
    def __str__(self): return self.name

class Challenge(AbstractSoftDeletableModel):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_challenges')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.ForeignKey(ChallengeStatus, on_delete=models.PROTECT, related_name='challenges')
    class Meta: verbose_name, verbose_name_plural = "Challenge", "Challenges"
    def __str__(self): return self.name

class Participant(AbstractSoftDeletableModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='participations')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='participants')
    join_date = models.DateTimeField(auto_now_add=True)
    current_streak = models.IntegerField(default=0)
    class Meta:
        verbose_name, verbose_name_plural = "Participant", "Participants"
        unique_together = ('user', 'challenge')
    def __str__(self): return f'{self.user.email} participates in "{self.challenge.name}"'

class CheckIn(AbstractSoftDeletableModel):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='check_ins')
    check_in_date = models.DateField()
    notes = models.TextField(blank=True)
    class Meta:
        verbose_name, verbose_name_plural = "Check-in", "Check-ins"
        unique_together = ('participant', 'check_in_date')
    def __str__(self): return f'Check-in from {self.participant.user.email} on {self.check_in_date}'

class Notification(AbstractSoftDeletableModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name, verbose_name_plural = "Notification", "Notifications"
        ordering = ['-created_at']
    def __str__(self): return f'Notification for {self.user.email}: "{self.message[:30]}..."'