from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import AddBrokerForm

from .models import Broker

def brokers_list(request):
    brokers = Broker.objects.all()
    return render(request, 'broker/brokers_list.html', {'brokers': brokers})

@login_required
def add_broker(request):
    if request.method == 'POST':
        form = AddBrokerForm(request.POST)

        if form.is_valid():
            broker = form.save(commit=False)
            broker.created_by = request.user
            broker.save()

            messages.success(request, 'El Broker fue creado exitosamente')

            return redirect('brokers_list')
        else:
            messages.error(request, 'Error al crear el Broker. Por favor, verifica los campos e intenta nuevamente.')
    else:
        form = AddBrokerForm()

    return render(request, 'broker/add_broker.html', {'form': form})

@login_required
def brokers_detail(request, pk):
    broker = get_object_or_404(Broker, pk=pk)

    return render(request, 'broker/brokers_detail.html', {'broker': broker})

@login_required
def brokers_edit(request, pk):
    broker = get_object_or_404(Broker, pk=pk)

    if request.method == 'POST':
        form = AddBrokerForm(request.POST, instance=broker)

        if form.is_valid():
            form.save()
            messages.success(request, 'El Broker fue modificado exitosamente')
            return redirect('brokers_list')
        else:
            messages.error(request, 'Error al modificar el Broker. Por favor, verifica los campos e intenta nuevamente.')
    else:
        form = AddBrokerForm(instance=broker)

    return render(request, 'broker/brokers_edit.html', {'form': form})

@login_required
def brokers_delete(request, pk):
    broker = get_object_or_404(Broker, pk=pk)
    broker.delete()

    messages.success(request, 'El Broker fue borrado exitosamente')

    return redirect('brokers_list')
