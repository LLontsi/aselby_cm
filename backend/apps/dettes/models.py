# TODO : Définir les modèles de l'application 'dettes'
# Référence : voir le document schema_bd_aselby.pdf pour la liste des tables et colonnes attendues

from django.db import models

class dette_listerouge(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    adherent_id = models.ForeignKey()
    config_exercice_id = models.ForeignKey()
    date_entree = models.datefield(auto_now_add)
    motif = models.TextField()
    montant_dette = models.DecimalField(14,2)
    vontant_garantie = models.DecimalField(14,2)
    est_solde = models.BooleanField()
    date_solde = models.DateField()
   
   class dette_remboursementdette(models.Model):
    ACTIF   = 'ACTIF'
    INACTIF = 'INACTIF'
    STATUT_CHOICES = [(ACTIF, 'Actif'), (INACTIF, 'Inactif')]

    id  = models.AutoField()
    liste_rouge_id = models.ForeignKey()
    date = models.DateField()
    montant = models.DecimalField(14,2)
    observations = models.TextField()
    