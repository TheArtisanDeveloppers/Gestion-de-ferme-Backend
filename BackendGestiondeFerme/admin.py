from django.contrib import admin

from .models import Responsable, Sorti, Aliment, Loge,Medicament, Type, Approvisionement, Animal,  Alimentation, Prise_medicament_animal

admin.site.site_header = "Gestion de Ferme Admin"
admin.site.site_title = "Gestion de Ferme Admin"
admin.site.index_title = "Bienvenue a page d'administration de la Gestion de Ferme"

admin.site.register(Responsable)
admin.site.register(Sorti)
admin.site.register(Aliment)
admin.site.register(Loge)
admin.site.register(Medicament)
admin.site.register(Type)
admin.site.register(Approvisionement)
admin.site.register(Animal)
admin.site.register(Alimentation)
admin.site.register(Prise_medicament_animal)
