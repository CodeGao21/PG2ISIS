from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import AddLeadForm
import datetime
from .models import Lead

from client.models import Client
from broker.models import Broker
from property.models import Property

@login_required
def leads_detail(request, pk):
    lead = Lead.objects.all().get(pk=pk)

    return render(request, 'lead/leads_detail.html', {'lead': lead})

@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead.delete()

    messages.success(request, 'El Lead fue borrado exitosamente')

    return redirect('leads_list')

@login_required
def leads_list(request):
    state = request.GET.get('state', '')
    status = request.GET.get('status', '')
    month = request.GET.get('month', '')
    year = request.GET.get('year', '')

    leads = Lead.objects.all()
    if state:
        leads = leads.filter(state=state)
    if status:
        leads = leads.filter(status=status)
    if month:
        leads = leads.filter(date__month=month)
    if year:
        leads = leads.filter(date__year=year)

    current_year = datetime.datetime.now().year
    years = range(current_year - 5, current_year + 1)  # últimos 5 años hasta el año actual

    context = {
        'leads': leads,
        'states': Lead.CHOICES_STATE,
        'statuses': Lead.CHOICES_STATUS,
        'selected_state': state,
        'selected_status': status,
        'selected_month': month,
        'selected_year': year,
        'years': years
    }

    return render(request, 'lead/leads_list.html', context)


@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    properties = Property.objects.all().order_by('name')  # Obtiene todas las propiedades disponibles
    brokers = Broker.objects.all().order_by('name')  # Obtiene todos los brokers disponibles

    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'El Lead fue modificado exitosamente')
            return redirect('leads_list')
        else:
            messages.error(request, 'Error al modificar el Lead. Por favor, verifica los campos e intenta nuevamente.')
    else:
        form = AddLeadForm(instance=lead)

    context = {
        'form': form,
        'lead': lead,
        'properties': properties,  # Pasa las propiedades al contexto
        'brokers': brokers,  # Pasa los brokers al contexto
    }
    return render(request, 'lead/leads_edit.html', context)


@login_required
def add_lead(request):
    properties = Property.objects.all().order_by('name')
    brokers = Broker.objects.all().order_by('name')

    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            form.save_m2m()  # This is needed to save ManyToMany and ForeignKey fields when using commit=False

            messages.success(request, 'El Lead fue creado exitosamente')
            return redirect('leads_list')
        else:
            messages.error(request, 'Error al crear el Lead. Por favor, verifica los campos e intenta nuevamente.')
    else:
        form = AddLeadForm()

    context = {
        'form': form,
        'properties': properties,
        'brokers': brokers
    }
    return render(request, 'lead/add_lead.html', context)

@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    
    # Actualizar estado del lead
    lead.status = 'Cliente'
    lead.state = 'Cerrado'
    lead.save()

    # Guardar datos relevantes del lead en la sesión
    request.session['lead_to_client'] = {
        'commercialname': lead.name,
        'emailcontact': lead.email,
        'description': lead.description,
        'phonecontact': lead.phone,
        'broker_id': lead.broker.id if lead.broker else '',
    }

    request.session['coming_from_lead_conversion'] = True

    return redirect('/dashboard/clients/add-client/')





