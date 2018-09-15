from django.db import models
from hyconhacks.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Paper(TimeStampedModel):

    segment = models.CharField(max_length=140, null=True)
    target = models.CharField(max_length=140, null=True)
    file_path = models.ImageField(null=True)
    sender = models.ForeignKey(user_models.User, on_delete=models.SET_NULL, null=True, related_name='sender')
    receiver = models.ForeignKey(user_models.User, on_delete=models.SET_NULL, null=True, related_name='receiver')
    incentive = models.FloatField(null=True)
    difficulty = models.CharField(max_length=140, null=True)
