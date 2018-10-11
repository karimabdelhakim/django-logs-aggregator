from django.conf import settings
from django.db import models

# Create your models here.
LOG_TYPES = (
    ('info', 'Info'),
    ('warning', 'Warning'),
    ('error', 'Error')
)


class LogManager(models.Manager):

    def get_user_logs(self, user):
        return self.get_queryset().filter(user=user)


class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=LOG_TYPES)
    message = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = LogManager()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.message)
