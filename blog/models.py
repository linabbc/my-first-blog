from django.db import models
from django.utils import timezone


class Post(models.Model):
    nom = models.TextField()
    prenom = models.TextField()
    adresse = models.TextField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nom, self.prenom, self.adresse