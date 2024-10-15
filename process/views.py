from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from property.models import Property
from .forms import AddProcessForm

from .models import Process

def processes_list(request):
    Process.update_durations()
    processes = Process.objects.all()
    return render(request,'process/processes_list.html', {
        'processes': processes
    })

@login_required
def add_process(request):
    if request.method == 'POST':
        form = AddProcessForm(request.POST)
        if form.is_valid():
            process = form.save(commit=False)
            process.created_by = request.user
            process.save()
            messages.success(request, 'La Actividad fue creada exitosamente')
            return redirect('processes_list')
        else:
            messages.error(request, 'Error al crear la Actividad. Por favor, revisa los errores en el formulario.')
    else:
        form = AddProcessForm()

    properties = Property.objects.all()

    return render(request, 'process/add_process.html', {
        'form': form,
        'properties': properties,
    })


@login_required
def processes_edit(request, pk):
    process = get_object_or_404(Process, pk=pk)
    if request.method == 'POST':
        form = AddProcessForm(request.POST, instance=process)
        if form.is_valid():
            form.save()
            messages.success(request, 'La Actividad fue modificada exitosamente')
            return redirect('processes_list')
        else:
            print(form.errors)
            messages.error(request, 'Error al crear la Actividad. Por favor, revisa los errores en el formulario.')
    else:
        form = AddProcessForm(instance=process)


    properties = Property.objects.all()

    return render(request, 'process/processes_edit.html', {
        'form': form,
        'properties': properties,
    })

@login_required
def processes_delete(request, pk):
    process = get_object_or_404(Process, pk=pk)
    process.delete()

    messages.success(request, 'La Actividad fue borrada exitosamente' )

    return redirect('processes_list')

@login_required
def processes_detail(request, pk):
    process= get_object_or_404(Process, pk=pk)

    return render(request, 'process/processes_detail.html', {
        'process': process
    })