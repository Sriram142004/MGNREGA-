import requests
from dashboard.models import DistrictPerformance
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fetch MGNREGA data for Uttar Pradesh'

    def handle(self, *args, **kwargs):
        url = "https://api.data.gov.in/resource/<your_resource_id>?format=json&filters[state_name]=UTTAR%20PRADESH&api-key=<your_api_key>"
        response = requests.get(url)
        data = response.json()['records']

        for record in data:
            DistrictPerformance.objects.update_or_create(
                district_name=record['district_name'],
                month=record['month'],
                year=int(record['year']),
                defaults={
                    'workers': int(record['workers']),
                    'funds_spent': float(record['funds_spent']),
                    'job_days_generated': int(record['job_days_generated'])
                }
            )
        self.stdout.write(self.style.SUCCESS('MGNREGA data updated!'))
