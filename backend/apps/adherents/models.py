# adherents/models.py
# STUB minimal — maintenu uniquement pour satisfaire la clé étrangère de users.Utilisateur
# TODO : Compléter avec tous les champs (voir schema_bd_aselby.pdf)

from django.db import models


class Adherent(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    matricule  = models.CharField(max_length=20, primary_key=True)
    nom_prenom = models.CharField(max_length=20)
    statut     = models.CharField(max_length=10, choices=STATUT_CHOICES, default=ACTIF)
    numero_ordre =models.IntegerField(unique=True)
    fonction = models.CharField(max_length=200)
    telephone1 = models.CharField(max_length=25)
    telephone2 = models.CharField(max_length=25)
    residence = models.CharField(max_length=20)
    date_adhesion = models.DateField()
    date_reception = models.DateField()
    statut = models.CharField(max_length=10)
    photo = models.ImageField()
    poste_bureau = models.CharField(max_length=100)
    note = models.TextField()
    date_creation = models.DateTimeField(auto_now_add)
    date_modification = models.dateTimeField(auto_now)    

    # TODO : Ajouter les autres champs (numero_ordre, fonction, telephone1, telephone2,
    # residence, date_adhesion, date_reception, photo, poste_bureau, notes,
    # date_creation, date_modification) — voir schema_bd_aselby.pdf

    class Meta:
        verbose_name = "Adhérent"

    def __str__(self):
        return f"{self.matricule} - {self.nom_prenom}"
