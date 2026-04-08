# TODO : Définir les modèles de l'application 'exercice'
# Référence : voir le document schema_bd_aselby.pdf pour la liste des tables et colonnes attendues

from django.db import models

class exercice_fichecassation(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    adherent_id = models.ForeignKey()
    config_exercice_id = models.ForeignKey()
    fonds_caisse = models.DecimalField(14,2)
    repartition_interet = models.DecimalField(12,2)
    epargne_cumules = models.DecimalField(14,2)
    repartition_penalites = models.DecimalField(12,2)
    repartition_collation= models.DecimalField(12,2)
    sanction = models.DecimalField(12,2)
    complement_mutuelle = models.DecimalField(12,2)
    complement_fonds = models.DecimalField(12,2)
    dette_pret = models.DecimalField(14,2)
    dette_foyer = models.DecimalField(12,2)
    montant_percu = models.DecimalField(14,2)
    moantant_percu_especes = models.DecimalField(14,2)
    montant_percu_cheque = models.DecimalField(14,2)
    reconduction = models.DecimalField(14,2)
    nouveau_fonds = models.DecimalField(14,2)
    est_valide = models.DecimalField(14,2)
    date_calcul = models.DateTimeField(auto_now)

    class exercice_synthesecompte(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    config_exercice_id = models.ForeignKey()
    report_fonds_caisse = models.DecimalField(14,2)
    entrees_fonds_caisse = models.DecimalField(14,2)
    sorties_fonds_caisse = models.DecimalField(14,2)
    report_fonds_roulement = models.DecimalField(12,2)
    entrees_fonds_roulement = models.DecimalField(12,2)
    sorties_fonds_roulement = models.DecimalField(12,2)
    report_fonds_exceptionnel = models.DecimalField(12,2)
    entrees_frais_exceptionnel = models.DecimalField(12,2)
    sorties_frais_exceptionnel = models.DecimalField(12,2)
    report_fonds_mutuelle = models.DecimalField(12,2)
    entrees_frais_mutuelle = models.DecimalField(12,2)
    sorties_frais_mutuelle = models.DecimalField(12,2)
    report_inscription = models.DecimalField(12,2)
    entrees_inscription = models.DecimalField(12,2)
    report_penalites = models.DecimalField(12,2)
    entrees_penalite = models.DecimalField(12,2)
    sorties_penalite = models.DecimalField(12,2)
    report_collation = models.DecimalField(12,2)
    entrees_collation = models.DecimalField(12,2)
    sorties_collation = models.DecimalField(12,2)
    report_foyer = models.DecimalField(12,2)
    entrees_foyer = models.DecimalField(12,2)
    sorties_foyer = models.DecimalField(12,2)
    date_calcul = models.DateTimeField(auto_now)