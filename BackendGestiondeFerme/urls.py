"""BackendGestiondeFerme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BackendGestiondeFerme import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('responsables/', views.responsables_list),
    path('responsables/<int:id>', views.responsables_detail),
    path('sortis/', views.sorti_list),
    path('sortis/<int:id>', views.sorti_detail),
    path('aliments/', views.aliment_list),
    path('aliments/<int:id>', views.aliment_detail),
    path('loges/', views.loge_list),
    path('loges/<int:id>', views.loge_detail),
    path('medicaments/', views.medicament_list),
    path('medicaments/<int:id>', views.medicament_list),
    path('types/', views.type_list),
    path('types/<int:id>', views.type_detail),
    path('approvisionement/', views.approvisionement_list),
    path('approvisionement/<int:id>', views.approvisionement_detail),
    path('animaux/', views.animal_list),
    path('animaux/<int:id>', views.animal_detail),
    path('alimentation/', views.aliment_list),
    path('alimentation/<int:id>', views.alimentation_detail),
    path('prise_medicaments/', views.prisemedicament_list),
    path('prise_medicaments/<int:id>', views.prisemedicament_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)