from django.db import models
from django.contrib.auth.models import User

from property.models import Property
from django.utils.timezone import now 

class Process(models.Model):

    name = models.CharField(max_length=255)
    prop = models.ForeignKey(Property, related_name='processes', on_delete=models.CASCADE, blank=True, null=True)
    stage = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    time = models.IntegerField(default=0)
    OnProgress= models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(default=now, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='processes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if self.start_date:
            if not self.OnProgress and self.end_date is None:
                # If OnProgress is False and end_date is not provided, set it to the current day.
                self.end_date = now()
            elif self.OnProgress:
                self.end_date = now()
                

            duration = self.end_date - self.start_date
            # Calculate the duration in days, including the fractional part of the last day.
            self.time = duration.days + duration.seconds / 86400

        super(Process, self).save(*args, **kwargs)


    @classmethod
    def update_durations(cls):
        # Filtra todas las instancias de Process que están en progreso.
        processes_in_progress = cls.objects.filter(OnProgress=True)
        for process in processes_in_progress:
            if process.start_date:
                # Si no se ha establecido una fecha de finalización, usa la fecha y hora actuales.
                end_time = process.end_date if process.end_date else now()
                duration = end_time - process.start_date
                process.time = duration.days + duration.seconds / 86400  # Conversión a días.
                process.save(update_fields=['time'])

    def __str__(self):
        return self.name

