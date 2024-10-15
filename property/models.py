from django.db import models
from django.contrib.auth.models import User
from society.models import Society
from client.models import Client
from datetime import date

class Property(models.Model):
    GOOD = 'Bueno'
    REPAIR = 'A Reparar'

    CHOICES_CONDITION = (
        (GOOD, 'Bueno'),
        (REPAIR, 'A Reparar'),
    )

    DISPONIBLE = 'Disponible'
    OCUPADO = 'Ocupado'

    CHOICES_STATE = (
        (DISPONIBLE, 'Disponible'),
        (OCUPADO, 'Ocupado'),
    )

    ENERO= 'Enero'
    FEBRERO='Febrero'
    MARZO='Marzo'
    ABRIL='Abril'
    MAYO='Mayo'
    JUNIO='Junio'
    JULIO='Julio'
    AGOSTO='Agosto'
    SEPTIEMBRE='Septiembre'
    OCTUBRE='Octubre'
    NOVIEMBRE='Noviembre'
    DICIEMBRE='Diciembre'

    CHOICES_MONTHS = (
        (ENERO, 'Enero'),
        (FEBRERO, 'Febrero'),
        (MARZO, 'Marzo'),
        (ABRIL, 'Abril'),
        (MAYO, 'Mayo'),
        (JUNIO, 'Junio'),
        (JULIO, 'Julio'),
        (AGOSTO, 'Agosto'),
        (SEPTIEMBRE, 'Septiembre'),
        (OCTUBRE, 'Octubre'),
        (NOVIEMBRE, 'Noviembre'),
        (DICIEMBRE, 'Diciembre'),
    )

    FCA='FCA'
    ADMINISTRACION='Administracion'

    PAYOPTIONS = (
        (FCA,'FCA'),
        (ADMINISTRACION, 'Administracion'),
    )

    SI = 'SI'
    NO = 'NO'

    POLIZAOPTIONS = (
        (SI,'SI'),
        (NO, 'NO'),
    )

    name = models.CharField(max_length=255)
    society = models.ForeignKey(Society, related_name='properties', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=10, choices=CHOICES_STATE, default=DISPONIBLE)
    currentlease = models.ForeignKey(Client, related_name='properties', on_delete=models.SET_NULL, null=True, blank=True)
    condition = models.CharField(max_length=10, choices=CHOICES_CONDITION, default=GOOD)
    parkings = models.IntegerField(default=0)
    area1 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    address = models.CharField(max_length=255, blank=True, null=True)
    admin=models.CharField(max_length=255, blank=True, null=True)
    adminemail=models.EmailField(blank=True, null=True)
    adminphone=models.CharField(max_length=15,blank=True, null=True)
    rentprice = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    mainteinprice = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    costxm2 = models.DecimalField(max_digits=10, decimal_places=2,  default= 0.0)
    maintxm2 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    maindescrp = models.TextField(blank=True, null=True)
    pay = models.CharField(max_length=20, choices=PAYOPTIONS, blank=True, null=True)
    poliza = models.CharField(max_length=20, choices=POLIZAOPTIONS, blank=True, null=True)
    deposit= models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    leasestart = models.DateField(blank=True, null=True)
    leasend = models.DateField(blank=True, null=True)
    increase = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    lastincrease = models.DateField(blank=True, null=True)
    renov = models.CharField(max_length=255, choices=CHOICES_MONTHS, blank=True, null=True)
    notifyrenew = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @classmethod
    def update_prices(cls):
        # Obtiene todas las instancias de Property
        all_properties = cls.objects.all()
        for property in all_properties:
            if property.lastincrease is not None and property.increase is not None:
                current_year = date.today().year
                last_increase_year = property.lastincrease.year

                # Verifica si el último aumento no fue en el año actual
                if last_increase_year < current_year:
                    # Calcula los nuevos valores incrementados
                    property.costxm2 = (property.costxm2 * property.increase) + property.costxm2
                    property.maintxm2 = (property.maintxm2 * property.increase) + property.maintxm2
                    property.rentprice = property.costxm2 * property.area1
                    property.mainteinprice = property.maintxm2 * property.area1
                    # Actualiza la fecha de último aumento al día actual
                    property.lastincrease = date.today()
                    # Guarda los cambios en el modelo
                    property.save()

    def __str__(self):
        return self.name

