# TODO : Définir les modèles de l'application 'mutuelle'
# Référence : voir le document schema_bd_aselby.pdf pour la liste des tables et colonnes attendues

from django.db import models

class mutuelle_cotisationmutuelle(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    adherent_id = models.ForeignKey()
    config_exercice_id = models.ForeignKey()
    mois = models.IntegerField()
    annee = models.IntegerField()
    montant_auto = models.DecimalField(12,2)
    
    class mutuelle_aidemutuelle(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    adherent_id = models.ForeignKey()
    config_exercice_id = models.ForeignKey()
    date = models.DateField()
    evenement = models.CharField(max_length=300)
    montant = models.DecimalField(12,2)