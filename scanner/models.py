from django.db import models

class IPAddress(models.Model):
    address = models.GenericIPAddressField(unique=True)
    status = models.CharField(max_length=20, default='Unknown')
    reputation_score = models.IntegerField(default=0) # تأكد أنه Integer
    severity = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low')
    country = models.CharField(max_length=100, default='Unknown')
    last_scan = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address