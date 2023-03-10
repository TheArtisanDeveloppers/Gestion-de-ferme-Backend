from django.db import models
    
class Responsable(models.Model):
    id_responsable = models.IntegerField()
    nom_responsable = models.CharField(max_length=100)
    prenom_responsable = models.CharField(max_length=100)
    poste_responsable = models.CharField(max_length=200)
    mot_passe_responsable = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nom_responsable + " "+ self.prenom_responsable

class Sorti(models.Model):
    id_sorti = models.IntegerField()
    id_responsable = models.ForeignKey(Responsable, on_delete=models.DO_NOTHING)
    nom_client_sorti = models.CharField(max_length=100)
    date_sorti = models.DateField()

    def __str__(self) -> str:
        return self.nom_client_sorti
    
class Aliment(models.Model):
    id_aliment = models.IntegerField()
    nom_aliment = models.CharField(max_length=500)
    quantite_aliment = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nom_aliment

class Loge(models.Model):
    id_loge = models.IntegerField()
    nom_loge = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nom_loge

class Medicament(models.Model):
    id_medicament = models.IntegerField()
    nom_medicament = models.CharField(max_length=100)
    quantite_medicament = models.IntegerField()

    def __str__(self) -> str:
        return self.nom_medicament

class Type(models.Model):
    id_type = models.IntegerField()
    nom_type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nom_type

class Approvisionement(models.Model):
    id_approvisionement = models.IntegerField()
    id_responsable = models.ForeignKey(Responsable, on_delete=models.DO_NOTHING)
    nom_approvisionneur_approvisionement = models.CharField(max_length=100)
    nombre_depart_approvisionement = models.IntegerField()
    nombre_arriver_approvisionement = models.IntegerField()
    date_approvisionement = models.DateField()

    def __str__(self) -> str:
        return self.nom_approvisionneur_approvisionement
    
class Animal(models.Model):
    id_animal = models.IntegerField()  
    race_animal = models.CharField(max_length=100)
    poids_animal = models.CharField(max_length=100)
    sexe_animal = models.CharField(max_length=100)
    ids_parents_de_animal = models.CharField(max_length=1000)
    ids_enfants_de_animal = models.CharField(max_length=1000)
    etat_animal = models.IntegerField()
    id_loge = models.ForeignKey(Loge, on_delete=models.DO_NOTHING)
    id_sorti = models.ForeignKey(Sorti, on_delete=models.DO_NOTHING)
    id_approvisionement = models.ForeignKey(Approvisionement, on_delete=models.DO_NOTHING)
    id_type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return str(self.id_animal),self.race_animal
    
class Alimentation(models.Model):
    id_responsable = models.ForeignKey(Responsable, on_delete=models.DO_NOTHING)
    id_aliment = models.ForeignKey(Aliment, on_delete=models.DO_NOTHING)
    id_loge = models.ForeignKey(Loge, on_delete=models.DO_NOTHING)
    date_alimentation = models.DateField()
    quantite = models.IntegerField()

    # def __str__(self) -> str:
    #     return self.quantite
    
class Prise_medicament_animal(models.Model):
    id_responsable = models.ForeignKey(Responsable, on_delete=models.DO_NOTHING)
    id_animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    id_medicament = models.ForeignKey(Medicament, on_delete=models.DO_NOTHING)
    quantite_prise_medicament_animal = models.IntegerField()
    date_prise_medicament_animal = models.DateField()

    def __str__(self) -> str:
        return self.id_animal + "  " + self.quantite_prise_medicament_animal
