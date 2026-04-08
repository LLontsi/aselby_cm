# TODO : Définir les modèles de l'application 'tontines'
# Référence : voir le document schema_bd_aselby.pdf pour la liste des tables et colonnes attendues

from django.db import models

class tontines_niveautontine(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    config_exercice_id = models.ForeignKey()
    code = models.CharField()
    taux_mensuel_part = models.DecimalField(12,2)
    versement_mensuel_part = models.DecimalField(12,2)
    diviseur_interet = models.IntegerField()

    class tontines_sessiontontine(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    niveau_id = models.ForeignKey()
    mois = models.IntegerField()
    annee = models.IntegerField()
    date_seance = models.DateField()
    montant_interet_bureau = models.DecimalField(12,2)
    est_cloture = booleanfied()

    class tontines_participationtontine(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    session = models.ForeignKey()    
    adherent_id = models.ForeignKey()
    nombre_parts = models.IntegerField()
    mode_versement = models.CharField(max_length=10)
    montant_verse = models.DecimalField(14,2)
    penalite_especes = models.DecimalField(10,2)
    penalite_echec = models.DecimalField(12,2)
    nb_echec_cumules = models.IntegerField()
    en_liste_rouge = models.BooleanField()
    complement_epargne = models.DecimalField(12,2)
    numero_cheque = models.CharField(max_length=50)
    a_obtenu_lot_principal = models.BooleanField()
    montant_lot_principal = models.DecimalField(14,2)
    interet_lot_principal = models.DecimalField(12,2)
    vente_petit_lot = models.DecimalField(14,2)
    interet_petit_lot = models.DecimalField(12,2)
    remboursement_petit_lot = models.DecimalField(12,2)
    mode_remboursement = models.CharField(max_length=100)

    