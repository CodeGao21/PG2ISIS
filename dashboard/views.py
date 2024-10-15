from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from broker.models import Broker
from process.models import Process
from property.models import Property
from lead.models import Lead
from django.db.models import Count, F, ExpressionWrapper, fields, Avg, Sum
from django.utils import timezone

from django.db.models import Count
from django.utils import timezone

@login_required
def dashboard(request):
    Property.update_prices()
    Process.update_durations()

    now = timezone.now()
    current_year = now.year
    current_month = now.month

    total_properties = Property.objects.count()
    occupied_properties = Property.objects.filter(state=Property.OCUPADO).count()
    occupancy_percentage = round((occupied_properties / total_properties) * 100 if total_properties > 0 else 0, 2)

    # Inicializa los conteos de status y state con 0 para asegurar que todos aparezcan
    lead_status_counts_init = {status[0]: 0 for status in Lead.CHOICES_STATUS}
    lead_state_counts_init = {state[0]: 0 for state in Lead.CHOICES_STATE}

    lead_status_from_db = Lead.objects.filter(date__year=current_year, date__month=current_month).values('status').annotate(count=Count('status'))
    lead_state_from_db = Lead.objects.filter(date__year=current_year, date__month=current_month).values('state').annotate(count=Count('state'))

    for status_count in lead_status_from_db:
        lead_status_counts_init[status_count['status']] = status_count['count']
    for state_count in lead_state_from_db:
        lead_state_counts_init[state_count['state']] = state_count['count']

    lead_status_counts_with_display = [{'status': key, 'count': value} for key, value in lead_status_counts_init.items()]
    lead_state_counts_with_display = [{'state': key, 'count': value} for key, value in lead_state_counts_init.items()]
    
    processes_ranking = Process.objects.values('name', 'prop__name').annotate(total_time=Sum('time')).order_by('-total_time')[:7]

    # Fetching and filtering brokers with more than 0 leads, excluding 'Directo'
    brokers_ranking = Lead.objects.filter(date__year=current_year, date__month=current_month)\
        .exclude(broker__name__iexact='Directo')\
        .values('broker__name')\
        .annotate(count=Count('broker__name'))\
        .filter(count__gt=0)\
        .order_by('-count')
    
    # Prepare the data for display
    brokers_ranking_with_display = [{'broker_name': broker['broker__name'], 'count': broker['count']}
                                    for broker in brokers_ranking]

    # Fetching and filtering 'fuentes' with more than 0 leads
    fuente_ranking = Lead.objects.filter(date__year=current_year, date__month=current_month)\
        .values('fuente')\
        .annotate(count=Count('fuente'))\
        .filter(count__gt=0)\
        .order_by('-count')
    
    # Prepare the data for display
    fuente_ranking_with_display = [{'fuente_name': fuente['fuente'], 'count': fuente['count']}
                                   for fuente in fuente_ranking]
    

    average_lease_duration = Property.objects.filter(state=Property.OCUPADO).annotate(
        duration=ExpressionWrapper(F('leasend') - F('leasestart'), output_field=fields.DurationField())
    ).aggregate(average_duration=Avg('duration'))
    average_duration_in_days = round((average_lease_duration.get('average_duration').days / 365.25), 2) if average_lease_duration.get('average_duration') else 0


    total_rented_area = Property.objects.filter(state=Property.OCUPADO).aggregate(total_area=Sum('area1'))['total_area']
    total_rented_area = total_rented_area if total_rented_area is not None else 0

    total_rent_income = Property.objects.filter(state=Property.OCUPADO).aggregate(total_rent=Sum('rentprice'))['total_rent']
    total_rent_income = round(total_rent_income,2) if total_rent_income is not None else 0

        # Cálculo del promedio de duración para procesos en la etapa "Búsqueda Cliente"
    average_search_client_duration = Process.objects.filter(stage="Búsqueda Cliente").aggregate(average_time=Avg('time'))

    # Obtener el valor promedio desde el resultado del aggregate, si no existe será 0
    average_search_client_duration_value = average_search_client_duration.get('average_time', 0)

    # Asegúrate de redondear el promedio a 2 decimales o al nivel de precisión deseado
    average_search_client_duration_value = round(average_search_client_duration_value, 2) if average_search_client_duration_value else 0

    context = {
        'total_properties': total_properties,
        'occupied_properties': occupied_properties,
        'occupancy_percentage': occupancy_percentage,
        'lead_status_counts': lead_status_counts_with_display,
        'lead_state_counts': lead_state_counts_with_display,
        'brokers_ranking': brokers_ranking_with_display,
        'fuente_ranking': fuente_ranking_with_display,
        'processes_ranking': processes_ranking,
        'average_duration_in_days': average_duration_in_days,
        'total_rented_area': total_rented_area,
        'total_rent_income': total_rent_income,
        'average_search_client_duration': average_search_client_duration_value,
    }

    return render(request, 'dashboard/dashboard.html', context)


