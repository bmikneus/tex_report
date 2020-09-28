from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
# Create your models here.
class Report(models.Model):

    PROBLEM_CHOICES = [
        ('Eyes', 'Eyes'),
        ('Mouth', 'Mouth'),
        ('Wrist', 'Wrist'),
        ('Hand', 'Hand'),
        ('Arm', 'Arm'),
        ('Forearm', 'Forearm'),
        ('Neck', 'Neck'),
        ('Nod', 'Nod'),
        ('Message', 'Message'),
        ('Other', 'Other'),

    ]
    problem = MultiSelectField(choices=PROBLEM_CHOICES)
    other = models.CharField(default="", null=True, max_length=50)
    description = models.TextField(default="", max_length=1000)
    problem_datetime = models.DateTimeField(default=timezone.now)
    reporter = models.CharField(default="", max_length=30)

    
