# TODO : Définir les modèles de l'application 'prets'
# Référence : voir le document schema_bd_aselby.pdf pour la liste des tables et colonnes attendues

from django.db import models

class pret_pret(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id = models.AutoField()
    adherent_id = models.ForeignKey()
    config_exercice_id = models.ForeignKey()
    montant_principal = models.DecimalFieldy(14,2)
    taux_mensuel = models.DecimalFieldy(5,2)
    nombre_mois = models.IntegerField()
    interet_total = models.DecimalFieldy(12,2)
    montant_total_du = models.DecimalFieldy(14,2)
    date_octroi = models.DateField()
    date_echeance = models.DateField()
    mode_versement = models.charfield(max_length=10)
    numero_cheque = models.charfield(max_length=50)
    statut = models.charfield(max_length=15)
    nbre_mois_retard = models.IntegerField()
    montant_rembourse = models.DecimalFieldy(14,2)
    est_demande_membre = models.BooleanFieldy()
    est_valid_bureau = models.BooleanFieldy()
    motif_demande = models.TextField()
    date_demande = models.DateTimeField()
    motif_validation = models.DateTimeField()