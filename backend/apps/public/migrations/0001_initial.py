
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [('users','0001_initial')]
    operations = [
        migrations.CreateModel('Annonce', fields=[
            ('id', models.BigAutoField(primary_key=True)),
            ('titre', models.CharField(max_length=300)),
            ('contenu', models.TextField()),
            ('date_publication', models.DateField(auto_now_add=True)),
            ('est_publiee', models.BooleanField(default=True)),
            ('date_creation', models.DateTimeField(auto_now_add=True)),
            ('auteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.utilisateur')),
        ], options={'ordering': ['-date_publication']}),
        migrations.CreateModel('Activite', fields=[
            ('id', models.BigAutoField(primary_key=True)),
            ('titre', models.CharField(max_length=300)),
            ('description', models.TextField()),
            ('date', models.DateField()),
            ('lieu', models.CharField(blank=True, max_length=200)),
            ('est_publiee', models.BooleanField(default=True)),
        ], options={'ordering': ['-date']}),
        migrations.CreateModel('FAQ', fields=[
            ('id', models.BigAutoField(primary_key=True)),
            ('question', models.CharField(max_length=500)),
            ('reponse', models.TextField()),
            ('ordre', models.IntegerField(default=0)),
            ('est_publiee', models.BooleanField(default=True)),
        ], options={'ordering': ['ordre']}),
        migrations.CreateModel('Contact', fields=[
            ('id', models.BigAutoField(primary_key=True)),
            ('ville', models.CharField(default='Yaoundé', max_length=100)),
            ('pays', models.CharField(default='Cameroun', max_length=100)),
            ('telephone', models.CharField(blank=True, max_length=20)),
            ('email', models.EmailField(blank=True)),
            ('adresse', models.TextField(blank=True)),
            ('horaires', models.TextField(blank=True)),
        ]),
    ]
