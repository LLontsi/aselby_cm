# context_processors.py
# NOTE : Le context processor config_exercice est désactivé temporairement
# car l'application parametrage n'est pas encore implémentée.
# Décommenter une fois parametrage.models.ConfigExercice créé.

def config_exercice(request):
    # from apps.parametrage.models import ConfigExercice
    # return {'config_exercice': ConfigExercice.get_exercice_courant()}
    return {'config_exercice': None}
