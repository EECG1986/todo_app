from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """Modelo que representa una tarea."""

    PENDING = 'pending'
    COMPLETED = 'completed'
    STATUS_CHOICES = [
        (PENDING, 'Pendiente'),
        (COMPLETED, 'Completada'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Ingrese el título de la tarea')
    description = models.TextField(help_text='Ingrese la descripción de la tarea')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING,
        help_text='Establezca el estado de la tarea'
    )

    def __str__(self):
        """Cadena para representar el objeto Task (en el sitio de administración, etc.)."""
        return self.title
