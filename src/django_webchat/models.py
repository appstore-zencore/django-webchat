from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class Talk(models.Model):
    sid = models.UUIDField(unique=True)
    name = models.CharField(max_length=16, null=True, blank=True)

class P2pTalk(Talk):
    pass

class GroupTalk(Talk):
    owner = models.ForeignKey("Member", on_delete=models.CASCADE, null=True, blank=True, related_name="messages")
    announcement = models.CharField(max_length=64, null=True, blank=True)

class Member(models.Model):
    session = models.ForeignKey(Talk, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="members")
    name = models.CharField(max_length=16, null=True, blank=True)

class Message(models.Model):
    session = models.ForeignKey(Talk, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="messages")
    time = models.DateTimeField()
    content = models.TextField()

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return str(self.pk)
