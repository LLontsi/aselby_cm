from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal

from apps.public.models import Annonce
from .forms import ConnexionForm, ReinitialisationMotDePasseForm, DemandePretForm

MOIS_FR = ['','Janvier','Février','Mars','Avril','Mai','Juin',
           'Juillet','Août','Septembre','Octobre','Novembre','Décembre']


# ---------------------------------------------------------------------------
# Helpers — imports optionnels (apps pas encore implémentées)
# ---------------------------------------------------------------------------

def _get_config():
    try:
        from apps.parametrage.models import ConfigExercice
        return ConfigExercice.get_exercice_courant()
    except Exception:
        return None

def _get_mouvement_fonds(adherent, mois, annee):
    try:
        from apps.fonds.models import MouvementFonds
        return MouvementFonds.objects.filter(adherent=adherent, mois=mois, annee=annee).first()
    except Exception:
        return None

def _get_mouvements_fonds_annee(adherent, annee):
    try:
        from apps.fonds.models import MouvementFonds
        return MouvementFonds.objects.filter(adherent=adherent, annee=annee).order_by('mois')
    except Exception:
        return []

def _get_participations_mois(adherent, mois, annee):
    try:
        from apps.tontines.models import ParticipationTontine, SessionTontine
        sessions = SessionTontine.objects.filter(mois=mois, annee=annee)
        return ParticipationTontine.objects.filter(
            adherent=adherent, session__in=sessions
        ).select_related('session__niveau')
    except Exception:
        return []

def _get_participations_annee(adherent, config):
    try:
        from apps.tontines.models import ParticipationTontine
        return ParticipationTontine.objects.filter(
            adherent=adherent, session__niveau__config_exercice=config
        ).select_related('session__niveau').order_by('session__mois')
    except Exception:
        return []

def _get_niveaux_tontine(config):
    try:
        from apps.tontines.models import NiveauTontine
        return NiveauTontine.objects.filter(config_exercice=config).order_by('taux_mensuel')
    except Exception:
        return []

def _get_pret_actif(adherent):
    try:
        from apps.prets.models import Pret
        return Pret.objects.filter(adherent=adherent, statut__in=[Pret.EN_COURS, 'EN_RETARD']).first()
    except Exception:
        return None

def _get_prets(adherent, config):
    try:
        from apps.prets.models import Pret
        return Pret.objects.filter(
            adherent=adherent, config_exercice=config
        ).prefetch_related('remboursements').order_by('-date_octroi')
    except Exception:
        return []

def _get_saisie_mois(adherent, mois, annee, config):
    try:
        from apps.saisie.models import TableauDeBord
        return TableauDeBord.objects.filter(adherent=adherent, mois=mois, annee=annee).first()
    except Exception:
        return None

def _get_saisies_annee(adherent, annee, config):
    try:
        from apps.saisie.models import TableauDeBord
        return TableauDeBord.objects.filter(adherent=adherent, annee=annee, config_exercice=config)
    except Exception:
        return []

def _get_fiche_cassation(adherent, config):
    try:
        from apps.exercice.models import FicheCassation
        return FicheCassation.objects.filter(adherent=adherent, config_exercice=config).first()
    except Exception:
        return None


def _ctx_membre(request):
    return {
        'config_exercice': _get_config(),
        'adherent': request.user.adherent,
    }


# ============================================================
# AUTH (fonctionnel sans les autres apps)
# ============================================================

def page_connexion(request):
    if request.user.is_authenticated:
        return redirect('public:accueil')
    form = ConnexionForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f"Bienvenue, {user.nom_complet} !")
        return redirect('public:accueil')
    return render(request, 'users/connexion.html', {'form': form})


def deconnexion(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('public:accueil')


@login_required
def changer_mot_de_passe(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        messages.success(request, "Mot de passe modifié avec succès.")
        return redirect('public:accueil')
    return render(request, 'users/changer_mot_de_passe.html', {'form': form})


def reinitialiser_mot_de_passe(request):
    form = ReinitialisationMotDePasseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        if user:
            user.set_password('aselby_2026')
            user.save()
            messages.success(request, "Mot de passe réinitialisé à 'aselby_2026'. Changez-le après connexion.")
            return redirect('users:connexion')
        else:
            messages.error(request, "Aucun compte trouvé avec ces informations.")
    return render(request, 'users/reinitialisation.html', {'form': form})


# ============================================================
# ESPACE MEMBRE (dépend des apps à implémenter)
# ============================================================

@login_required
def mon_espace(request):
    if request.user.est_bureau:
        return redirect('public:accueil')
    adherent = request.user.adherent
    if not adherent:
        messages.error(request, "Compte non lié à un adhérent.")
        return redirect('public:accueil')

    config = _get_config()
    now    = timezone.now()
    mois   = now.month
    annee  = now.year

    fonds_courant       = _get_mouvement_fonds(adherent, mois, annee)
    participations_mois = _get_participations_mois(adherent, mois, annee)
    nb_parts_total      = sum(p.nombre_parts for p in participations_mois)
    pret_en_cours       = _get_pret_actif(adherent)
    saisie_mois         = _get_saisie_mois(adherent, mois, annee, config)
    saisies_annee       = _get_saisies_annee(adherent, annee, config)
    nb_mois_saisis      = len(list(saisies_annee))
    liste_rouge         = getattr(adherent, 'liste_rouge', None)
    annonces_recentes   = Annonce.objects.filter(est_publiee=True).order_by('-date_publication')[:3]

    ctx = _ctx_membre(request)
    ctx.update({
        'fonds_courant'        : fonds_courant,
        'nb_parts_total'       : nb_parts_total,
        'participations_mois'  : participations_mois,
        'pret_en_cours'        : pret_en_cours,
        'liste_rouge'          : liste_rouge,
        'saisie_mois'          : saisie_mois,
        'nb_mois_saisis'       : nb_mois_saisis,
        'annonces_recentes'    : annonces_recentes,
        'mois_courant_label'   : f"{MOIS_FR[mois]} {annee}",
    })
    return render(request, 'membre/mon_espace.html', ctx)


@login_required
def mon_fonds(request):
    if request.user.est_bureau:
        return redirect('public:accueil')
    adherent  = request.user.adherent
    config    = _get_config()
    annee     = config.annee if config else timezone.now().year

    mouvements       = _get_mouvements_fonds_annee(adherent, annee)
    mouvements_list  = list(mouvements)
    dernier          = mouvements_list[-1] if mouvements_list else None
    total_interets   = sum(getattr(m, 'interet_attribue', Decimal('0')) for m in mouvements_list)
    saisies          = _get_saisies_annee(adherent, annee, config)

    ctx = _ctx_membre(request)
    ctx.update({
        'mouvements'       : mouvements,
        'dernier_mouvement': dernier,
        'total_interets'   : total_interets,
        'nb_mois_saisis'   : len(mouvements_list),
        'saisies'          : saisies,
        'liste_rouge'      : getattr(adherent, 'liste_rouge', None),
    })
    return render(request, 'membre/mon_fonds.html', ctx)


@login_required
def mes_tontines(request):
    if request.user.est_bureau:
        return redirect('public:accueil')
    adherent       = request.user.adherent
    config         = _get_config()
    participations = _get_participations_annee(adherent, config)
    niveaux        = _get_niveaux_tontine(config)

    niveaux_participation = []
    for niv in niveaux:
        parts = [p for p in participations if p.session.niveau == niv]
        if parts:
            niveaux_participation.append({'niveau': niv, 'participations': parts})

    ctx = _ctx_membre(request)
    ctx.update({
        'participations'        : participations,
        'niveaux_participation' : niveaux_participation,
        'nb_participations'     : len(list(participations)),
        'nb_parts_total'        : sum(p.nombre_parts for p in participations),
        'nb_lots_obtenus'       : sum(1 for p in participations if p.a_obtenu_lot_principal),
        'nb_mois_banque'        : sum(1 for p in participations if p.mode_versement == 'BANQUE'),
    })
    return render(request, 'membre/mes_tontines.html', ctx)


@login_required
def mes_prets(request):
    if request.user.est_bureau:
        return redirect('public:accueil')
    config = _get_config()
    ctx    = _ctx_membre(request)
    ctx['prets'] = _get_prets(request.user.adherent, config)
    return render(request, 'membre/mes_prets.html', ctx)


@login_required
def demander_pret(request):
    if request.user.est_bureau:
        return redirect('public:accueil')
    adherent  = request.user.adherent
    config    = _get_config()
    pret_actif = _get_pret_actif(adherent)

    if request.method == 'POST' and not pret_actif:
        form = DemandePretForm(request.POST, config=config)
        if form.is_valid():
            try:
                from apps.prets.models import Pret
                pret = form.save(commit=False)
                pret.adherent           = adherent
                pret.config_exercice    = config
                pret.taux_mensuel       = config.taux_interet_pret_mensuel
                pret.est_demande_membre = True
                pret.est_valide_bureau  = False
                pret.date_demande       = timezone.now()
                pret.statut             = Pret.EN_COURS
                pret.save()
                messages.success(request, "Votre demande de prêt a été envoyée au bureau.")
                return redirect('membre:mes_prets')
            except Exception:
                messages.error(request, "Impossible de créer le prêt : application non disponible.")
    else:
        form = DemandePretForm(config=config)

    ctx = _ctx_membre(request)
    ctx.update({'form': form, 'pret_actif': pret_actif, 'config': config})
    return render(request, 'membre/demander_pret.html', ctx)


@login_required
def ma_situation(request):
    if request.user.est_bureau:
        return redirect('public:accueil')
    adherent   = request.user.adherent
    config     = _get_config()
    annee      = config.annee if config else timezone.now().year

    fiche_cassation  = _get_fiche_cassation(adherent, config)
    mouvements       = list(_get_mouvements_fonds_annee(adherent, annee))
    dernier          = mouvements[-1] if mouvements else None
    capital_total    = getattr(dernier, 'capital_compose', Decimal('0')) if dernier else Decimal('0')
    pret_actif       = _get_pret_actif(adherent)
    dette_pret       = pret_actif.solde_restant if pret_actif else Decimal('0')
    participations   = list(_get_participations_annee(adherent, config))
    nb_parts_total   = sum(p.nombre_parts for p in participations)
    saisies          = list(_get_saisies_annee(adherent, annee, config))

    ctx = _ctx_membre(request)
    ctx.update({
        'fiche_cassation' : fiche_cassation,
        'capital_total'   : capital_total,
        'dette_pret'      : dette_pret,
        'nb_parts_total'  : nb_parts_total,
        'nb_mois_saisis'  : len(saisies),
        'nb_mois_banque'  : sum(1 for s in saisies if getattr(s, 'mode_versement', '') == 'BANQUE'),
        'nb_mois_especes' : sum(1 for s in saisies if getattr(s, 'mode_versement', '') == 'ESPECES'),
        'nb_echecs'       : sum(1 for s in saisies if getattr(s, 'mode_versement', '') == 'ECHEC'),
        'liste_rouge'     : getattr(adherent, 'liste_rouge', None),
    })
    return render(request, 'membre/ma_situation.html', ctx)
