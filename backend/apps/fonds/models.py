# TODO : Définir les modèles de l'application 'fonds'
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
    reconduction = models.DecimalField(14,2)
    retrait_partiel = models.DecimalField(14,2)
    capital_compose_precedent = models.DecimalField(14,2)
    reste = models.DecimalField(14,2)
    epargne_nette = models.DecimalField(14,2)
    fonds_roulement = models.DecimalField(10,2)
    frais_exceptionnel = models.DecimalField(10,2)
    collation= models.DecimalField(10,2)
    fonds_definitif = models.DecimalField(14,2)
    base_calcul_interet = models.DecimalField(14,2)
    interet_attribue = models.DecimalField(12,2)
    capital_compose = models.DecimalField(14,2)
    sanction = models.DecimalField(14,2)
    date_calcul= models.DateTimeField(auto_now)



    class fonds_reservemensuelle(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    config_exercice_id = models.ForeignKey()
    mois = models.IntegerField()
    annee = models.IntegerField()
    pool_interet = models.DecimalField(14,2)
    total_bases_eligibles = models.DecimalField(14,2)
    nb_adherents_eligibles = models.IntegerField(14,2)
    est_reparti = models.BooleanField()

    