from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from collections import defaultdict

from property.models import Property
from .forms import AddSocietyForm

from .models import Society
from process.models import Process

def propierties_process_detail(request, pk):
    Process.update_durations()
    property = get_object_or_404(Property, pk=pk)
    processes = property.processes.all()

    # Group processes by type
    processes_by_type = defaultdict(list)
    sums_by_type = defaultdict(Decimal)

    for process in processes:
        processes_by_type[process.stage].append(process)
        sums_by_type[process.stage] += process.time

    return render(request, 'society/properties_process_detail.html', {
        'property': property, 
        'processes_by_type': dict(processes_by_type),
        'sums_by_type': dict(sums_by_type)
    })

def societies_list(request):
    societies = Society.objects.all()
    return render(request, 'society/societies_list.html', {'societies': societies})

@login_required
def add_society(request):
    if request.method == 'POST':
        form = AddSocietyForm(request.POST)

        if form.is_valid():
            society = form.save(commit=False)
            society.created_by = request.user
            society.save()

            messages.success(request, 'La Sociedad fue creada exitosamente')

            return redirect('societies_list')
        else:
            messages.error(request, 'Error al crear la Sociedad. Por favor, verifica los campos e intenta nuevamente.')
    else:
        form = AddSocietyForm()

    return render(request, 'society/add_society.html', {'form': form})

@login_required
def societies_detail(request, pk):
    society = get_object_or_404(Society, pk=pk)

    return render(request, 'society/societies_detail.html', {'society': society})

@login_required
def societies_edit(request, pk):
    society = get_object_or_404(Society, pk=pk)

    if request.method == 'POST':
        form = AddSocietyForm(request.POST, instance=society)

        if form.is_valid():
            form.save()
            messages.success(request, 'La Sociedad fue modificada exitosamente')
            return redirect('societies_list')
        else:
            messages.error(request, 'Error al modificar la Sociedad. Por favor, verifica los campos e intenta nuevamente.')
    else:
        form = AddSocietyForm(instance=society)

    return render(request, 'society/societies_edit.html', {'form': form})

@login_required
def societies_delete(request, pk):
    society = get_object_or_404(Society, pk=pk)
    society.delete()

    messages.success(request, 'La Sociedad fue borrada exitosamente')

    return redirect('societies_list')
