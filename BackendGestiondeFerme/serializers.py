from rest_framework import serializers
from .models import Responsable, Sorti, Aliment, Loge, Medicament, Type, Approvisionement, Animal, Alimentation, Prise_medicament_animal

class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = ['id_responsable', 'nom_responsable', 'prenom_responsable',
                  'poste_responsable', 'mot_passe_responsable']


class SortiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sorti
        fields = ['id_sorti', 'id_responsable','nom_client_sorti', 'date_sorti']


class AlimentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Aliment
        fields = ['id_aliment', 'nom_aliment', 'quantite_aliment']


class LogeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loge
        fields = ['id_loge', 'nom_loge']


class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = ['id_medicament', 'nom_medicament', 'quantite_medicament']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id_type', 'nom_type',]


class ApprovisionementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approvisionement
        fields = ['id_approvisionement', 'id_responsable', 'nom_approvisionneur_approvisionement','nombre_depart_approvisionement', 'nombre_arriver_approvisionement', 'date_approvisionement']


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id_animal', 'race_animal', 'poids_animal', 'sexe_animal',
                  'ids_parents_de_animal', 'ids_enfants_de_animal', 'etat_animal', 'id_loge', 'id_sorti', 'id_approvisionement', 'id_type']


class AlimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentation
        fields = ['id_responsable', 'id_aliment','id_loge', 'date_alimentation', 'quantite']


class Prise_medicament_animalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prise_medicament_animal
        fields = ['id_responsable', 'id_animal', 'id_medicament', 'quantite_prise_medicament_animal', 'date_prise_medicament_animal']
