# TODO : Définir les modèles de l'application 'parametrage'
# Référence : voir le document schema_bd_aselby.pdf pour la liste des tables et colonnes attendues

from django.db import models

class parametrage_configexercice(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    annee = models.IntegerField()
    est_ouvert = models.BooleanField()
    date_ouverture = models.DateField()
    date_cloture = models.DateField()
    taux_t35 = models.DecimalField(12,2)
    versement_t35 = models.DecimalField(12,2)
    taux_t75 = models.DecimalField(12,2)
    taux_t100 = models.DecimalField(12,2)
    diviseur_interet_t35 = models.IntegerField()
    seuil_eligible_interet = models.DecimalField(12,2)
    fond_roulement_mensuel = models.DecimalField(10,2)
    frais_exceptionnel_mensuel = models.DecimalField(10,2)
    collation_mensuel = models.DecimalField(10,2)
    complement_fonds_fin_exercice = models.DecimalField(12,2)
    penalite_especes = models.DecimalField(10,2)
    penalite_especes_active = models.BooleanField()
    pourcentage_penalite_echeance = models.DecimalField(5,2) 
    nb_echecs_max_avant_list = models.IntegerField() 
    taux_interet_pret_mensuel = models.DecimalField(5,2) 
    majoration_interet_retard_mois_1 = models.DecimalField(5,2) 
    majoration_interet_retard_mois_2 = models.DecimalField(5,2) 
    contribution_foyer_lot_principal = models.DecimalField(12,2)
    complement_mutuelle_fin = models.DecimalField(12,2)




    