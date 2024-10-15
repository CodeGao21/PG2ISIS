from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import AddClientForm

from .models import Client
from .models import Broker

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'client/clients_list.html', {'clients': clients})

@login_required
@login_required
def add_client(request):
    brokers = Broker.objects.all()

    # Inicializa initial_data como vacío si no vienes de convertir un lead
    initial_data = {}

    # Solo usa la información de lead si específicamente venimos de la conversión de un lead
    if 'coming_from_lead_conversion' in request.session and request.session['coming_from_lead_conversion']:
        initial_data = request.session.get('lead_to_client', {})
        if 'broker_id' in initial_data:
            # Asegúrate de convertir 'broker_id' a una instancia de Broker para el formulario
            initial_data['broker'] = initial_data.pop('broker_id')

        # Limpia los datos relevantes de la sesión inmediatamente después de usarlos
        request.session.pop('lead_to_client', None)
        request.session['coming_from_lead_conversion'] = False

    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()

            messages.success(request, 'El Cliente fue creado exitosamente')
            return redirect('clients_list')
        else:
            messages.error(request, 'Error al crear el cliente. Por favor, verifica los campos e intenta nuevamente.')
    else:
        form = AddClientForm(initial=initial_data)

    return render(request, 'client/add_client.html', {'form': form, 'brokers': brokers})

@login_required
def clients_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)

    return render(request, 'client/clients_detail.html', {'client': client})

def clients_edit(request, pk):
    broker = get_object_or_404(Client, pk=pk)
    brokers = Broker.objects.all()  

    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=broker)

        if form.is_valid():
            form.save()
            messages.success(request, 'El Cliente fue modificado exitosamente')
            return redirect('clients_list')
        else:
            messages.error(request, 'Error al modificar el cliente. Por favor, verifica los campos e intenta nuevamente.')
    else:
        form = AddClientForm(instance=broker)

    return render(request, 'client/clients_edit.html', {'form': form, 'brokers': brokers})

@login_required
def clients_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()

    messages.success(request, 'El Cliente fue borrado exitosamente')
    return redirect('clients_list')


