from django.db import models
from django.conf import settings


class Favourite(models.Model):
    # Detalles del personaje.
    name = models.CharField(max_length=200)  # Nombre del personaje
    gender = models.CharField(max_length=50)  # Género
    house = models.CharField(max_length=100, null=True, blank=True)  # Casa (puede ser nulo)
    actor = models.CharField(max_length=200, null=True, blank=True)  # Actor (puede ser nulo)
    image = models.URLField()  # URL de la imagen

    # Asociamos el favorito con el usuario que lo guarda.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        # Restringe duplicados: un mismo usuario no puede guardar el mismo personaje varias veces.
        unique_together = (('user', 'name', 'actor'),)

    def __str__(self):
        return (f"{self.name} - Casa: {self.house if self.house else 'Desconocida'} "
                f"(Actor: {self.actor if self.actor else 'Desconocido'}) - "
                f"User: {self.user.username}")
