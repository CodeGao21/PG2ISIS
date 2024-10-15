from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from datetime import date

from society.models import Society
from client.models import Client
from .forms import AddPropertyForm
from .models import Property

@login_required
def properties_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)

    return render(request, 'property/properties_detail.html', {
        'property': property
    })

@login_required
def properties_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    property.delete()

    messages.success(request, 'La Propiedad fue borrada exitosamente')

    return redirect('properties_list')

@login_required
def properties_list(request):
    Property.update_prices()
    properties = Property.objects.all()

    return render(request, 'property/properties_list.html', {'properties': properties})


@login_required
def properties_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    societies = Society.objects.all()
    clients = Client.objects.all()  # Fetch all clients

    if request.method == 'POST':
        form = AddPropertyForm(request.POST, instance=property)

        if form.is_valid():
            property = form.save(commit=False)

            if property.increase is None:
                property.increase=0

            if property.area1 != 0:
                 property.costxm2 = property.rentprice/property.area1
                 property.maintxm2 = property.mainteinprice/property.area1  
            else:
                property.costxm2 = 0
                property.maintxm2 = 0 

            if property.state == 'Disponible':
                # Set fields to None
                property.currentlease = None
                property.pay = None
                property.leasestart = None
                property.leasend = None
                property.increase = 0
                property.lastincrease= None
                property.renov = None
                property.notifyrenew = 0
                property.poliza=None
                property.deposit= 0
            
            # Save the property after making all changes
            property.save()

            messages.success(request, 'La Propiedad fue modificada exitosamente')
            return redirect('properties_list')
        else:
            print(form.errors)
            messages.error(request, 'Error al modificar la Propiedad. Por favor, revisa los errores en el formulario.')
    else:
        form = AddPropertyForm(instance=property)

    return render(request, 'property/properties_edit.html', {'form': form, 'societies': societies, 'clients': clients})

@login_required
def add_property(request):
    societies = Society.objects.all()  # Obtain all existing societies
    clients = Client.objects.all()  # Fetch all clients

    if request.method == 'POST':
        form = AddPropertyForm(request.POST)

        if form.is_valid():
            property = form.save(commit=False)
            property.created_by = request.user

            if property.increase is None:
                property.increase=0

            if property.area1 != 0:
                 property.costxm2 = property.rentprice/property.area1
                 property.maintxm2 = property.mainteinprice/property.area1  
            else:
                property.costxm2 = 0
                property.maintxm2 = 0     

            property.save()

            messages.success(request, 'La Propiedad fue creada exitosamente')

            return redirect('properties_list')
        else:
            # Add error messages in Spanish
            messages.error(request, 'Error al crear la Propiedad. Por favor, revisa los errores en el formulario.')
    else:
        form = AddPropertyForm()

    return render(request, 'property/add_property.html', {'form': form, 'societies': societies, 'clients': clients})
