from django.urls import path
from .views import dashboard_view, district_data

urlpatterns = [
    # Dashboard page
    path('', dashboard_view, name='dashboard'),

    # API endpoint (returns JSON for charts)
    path('districts/', district_data, name='districts-data'),
]
