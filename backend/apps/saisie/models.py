# TODO : Définir les modèles de l'application 'saisie'
# Référence : voir le document schema_bd_aselby.pdf pour la liste des tables et colonnes attendues

from django.db import models

class fonds_mouvementfonds(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    adherent_id = models.ForeignKey()
    config_exercice_id = models.ForeignKey()
    mois = models.IntegerField()
    annee = models.IntegerField()
    # versement

    versement_banque = models.DecimalField(14,2)
    versement_especes = models.DecimalField(14,2)
    autre_versement = models.DecimalField(14,2)
    complement_epargne = models.DecimalField(14,2)
    mode_versement = models.CharField(max_length=10)

    # cotisation

    inscription = models.DecimalField(12,2)
    mutuelle = models.DecimalField(12,2)
    contribution_foyer = models.DecimalField(12,2)
    don_foyer_volontaire = models.DecimalField(12,2)
    sanction = models.DecimalField(12,2)

    # pret

    pret_fonds = models.DecimalField(14,2)
    remboursement_pret = models.DecimalField(14,2)
    mode_pret = models.CharField(max_length=10)
    numero_cheque_pret = models.CharField(max_length=10)
    retrait_partiel_fonds = models.DecimalField(14,2)

    # champ_calcul

    bonus_malus = models.DecimalField(14,2)
    montant_engagement = models.DecimalField(14,2)
    penalite_especes_applique = models.DecimalField(10,2)
    penalite_echec_appliaue = models.DecimalField(12,2)
    contribution_foyer_auto = models.DecimalField(12,2)
    reste = models.DecimalField(14,2)
    libelle_depense = models.CharField(max_length=200)
    compte_depenses = models.CharField(max_length=10)
    autres_depenses = models.DecimalField(12,2)
    est_valide = models.BooleanField()
    date_saisie = models.DateTimeField(auto_now_add=)
    date_modification = models.DateTimeField(auto_now_add=)




   