from django.db import models

# Create your models here.


class AddToListModel(models.Model):
    PRIORITY_CHOICES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )

    title = models.CharField(max_length=30)
    priorityIs = models.CharField(max_length=30, choices=PRIORITY_CHOICES)
    endDate = models.DateTimeField(max_length=50)
    description = models.CharField(max_length=50)

# def __self__(self):
#     return self.title