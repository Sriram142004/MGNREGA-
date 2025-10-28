from django.db import models

class DistrictPerformance(models.Model):
    district_name = models.CharField(max_length=100)
    workers = models.IntegerField()
    job_days_generated = models.IntegerField()
    funds_spent = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.district_name} ({self.workers})"
