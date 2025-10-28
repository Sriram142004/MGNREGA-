from django.shortcuts import render
from django.http import JsonResponse
from .models import DistrictPerformance
from django.db.models import Sum
from django.utils.timezone import localtime
import json

def dashboard_view(request):
    # Fetch data from model
    data = DistrictPerformance.objects.all().order_by('district_name')

    # Compute summary stats
    total_districts = data.values('district_name').distinct().count()
    total_workers = data.aggregate(Sum('workers'))['workers__sum'] or 0
    total_job_days = data.aggregate(Sum('job_days_generated'))['job_days_generated__sum'] or 0
    total_funds_spent = data.aggregate(Sum('funds_spent'))['funds_spent__sum'] or 0

    try:
        last_updated = localtime(data.latest('updated_at').updated_at).strftime("%Y-%m-%d %H:%M")
    except Exception:
        last_updated = "N/A"

    # Convert to JSON lists for frontend use
    district_names = list(data.values_list('district_name', flat=True))
    workers_data = list(data.values_list('workers', flat=True))
    funds_data = list(data.values_list('funds_spent', flat=True))

    context = {
        'total_districts': total_districts,
        'total_workers': total_workers,
        'total_job_days': total_job_days,
        'total_funds_spent': total_funds_spent,
        'district_names_json': json.dumps(district_names),
        'workers_data_json': json.dumps(workers_data),
        'funds_data_json': json.dumps(funds_data),
        'last_updated': last_updated,
    }
    return render(request, 'dashboard/index.html', context)


# API endpoint for JSON data
def district_data(request):
    data = list(DistrictPerformance.objects.values(
        'district_name', 'workers', 'funds_spent'
    ))
    return JsonResponse(data, safe=False)
