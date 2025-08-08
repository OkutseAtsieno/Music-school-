from django.db import models

class Enrollment(models.Model):
    MODE_CHOICES = [
        ('online', 'Online'),
        ('physical', 'Physical'),
        ('hybrid', 'Hybrid'),
    ]

    SCHEDULE_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('weekend', 'Weekend'),
    ]

    GUITAR_TYPE_CHOICES = [
        ('acoustic', 'Acoustic'),
        ('lead', 'Lead/Solo'),
        ('bass', 'Bass'),
    ]

    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    guardians_phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    mode = models.CharField(max_length=20, choices=MODE_CHOICES)
    instrument = models.CharField(max_length=50)
    guitar_type = models.CharField(max_length=50, choices=GUITAR_TYPE_CHOICES, blank=True, null=True)
    schedule = models.CharField(max_length=20, choices=SCHEDULE_CHOICES)
    
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.instrument}"
