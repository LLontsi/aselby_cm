# TODO : Définir les modèles de l'application 'banque'
# Référence : voir le document schema_bd_aselby.pdf pour la liste des tables et colonnes attendues

from django.db import models

class banque_historiquebancaire(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    adherent_id = models.ForeignKey()
    config_exercice_id = models.ForeignKey()
    mois = models.IntegerField()
    annee = models.IntegerField()
    versement_tontine = models.DecimalField(14,2)
    versement_especes = models.DecimalField(14,2)
    versement_banque = models.DecimalField(14,2)
    autre_versement = models.DecimalField(14,2)
    montant_engagement = models.DecimalField(14,2)
    agio = models.DecimalField(14,2)

class banque_cheque(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    adherent_id = models.ForeignKey()
    config_exercice_id = models.ForeignKey()
    mois = models.IntegerField()
    annee = models.IntegerField()
    numero = models.CharField(max_length=50)
    montant = models.DecimalField(14,2)
    affectation = models.models.CharField(max_length=20)
    
    