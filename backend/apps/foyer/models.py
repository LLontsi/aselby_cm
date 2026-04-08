# TODO : Définir les modèles de l'application 'foyer'
# Référence : voir le document schema_bd_aselby.pdf pour la liste des tables et colonnes attendues

from django.db import models

 class foyer_contributionfoyer(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    adherent_id = models.ForeignKey()
    config_exercice_id = models.ForeignKey()
    mois = models.IntegerField()
    annee = models.IntegerField()
    montant_auto = models.DecimalField(12,2)
    don_volontaire = models.DecimalField(12,2)
   