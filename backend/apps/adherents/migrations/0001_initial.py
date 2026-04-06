from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Adherent',
            fields=[
                ('matricule', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nom_prenom', models.CharField(max_length=200)),
                ('statut', models.CharField(
                    choices=[('ACTIF', 'Actif'), ('INACTIF', 'Inactif')],
                    default='ACTIF', max_length=10
                )),
            ],
            options={
                'verbose_name': 'Adhérent',
            },
        ),
    ]
