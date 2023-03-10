from .models import Responsable, Sorti, Aliment, Loge,Medicament, Type, Approvisionement, Animal, Alimentation, Prise_medicament_animal
from django.http import JsonResponse
from .serializers import ResponsableSerializer, SortiSerializer, AlimentSerializer, LogeSerializer, MedicamentSerializer, TypeSerializer, ApprovisionementSerializer, AnimalSerializer, AlimentationSerializer, Prise_medicament_animalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#RESPONSABLES   
@api_view(['GET', 'POST'])
def responsables_list(request):
    if request.method == 'GET':
        responsables = Responsable.objects.all()
        responsables_serialized = ResponsableSerializer(responsables, many=True)
        return JsonResponse({"responsables":responsables_serialized.data}, safe=False)
    if request.method == 'POST':
        serializer = ResponsableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def responsables_detail(request, id):
    try:
        responsable = Responsable.objects.get(pk=id)
    except Responsable.DoesNotExist:
        return JsonResponse({"error" : "Le responsable n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        responsable_serialized = ResponsableSerializer(responsable)
        return JsonResponse(responsable_serialized.data, safe=False)
    
    elif request.method == 'PUT':
        serializer = ResponsableSerializer(responsable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        responsable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#SORTI
@api_view(['GET', 'POST'])
def sorti_list(request):
    if request.method == 'GET':
        values = Sorti.objects.all()
        values_serialized = SortiSerializer(
            values, many=True)
        return JsonResponse({"sortis": values_serialized.data}, safe=False)
    if request.method == 'POST':
        serializer = SortiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def sorti_detail(request, id):
    try:
        value = Sorti.objects.get(pk=id)
    except Sorti.DoesNotExist:
        return JsonResponse({"error": "La sorti n'existe pas dans la bd"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        value_serialized = SortiSerializer(value)
        return JsonResponse(value_serialized.data, safe=False)
    elif request.method == 'PUT':
        serializer = SortiSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ALIMENT
@api_view(['GET', 'POST'])
def aliment_list(request):
    if request.method == 'GET':
        values = Aliment.objects.all()
        values_serialized = AlimentSerializer(
            values, many=True)
        return JsonResponse({"aliments": values_serialized.data}, safe=False)
    if request.method == 'POST':
        serializer = AlimentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def aliment_detail(request, id):
    try:
        value = Aliment.objects.get(pk=id)
    except Aliment.DoesNotExist:
        return JsonResponse({"error": "L'aliment n'existe pas dans la bd"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        responsable_serialized = AlimentSerializer(value)
        return JsonResponse(responsable_serialized.data, safe=False)
    elif request.method == 'PUT':
        serializer = AlimentSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# LOGE
@api_view(['GET', 'POST'])
def loge_list(request):
    if request.method == 'GET':
        values = Loge.objects.all()
        values_serialized = LogeSerializer(
            values, many=True)
        return JsonResponse({"loges": values_serialized.data}, safe=False)
    if request.method == 'POST':
        serializer = LogeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def loge_detail(request, id):
    try:
        value = Loge.objects.get(pk=id)
    except Loge.DoesNotExist:
        return JsonResponse({"error": "La loge n'existe pas dans la bd"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        responsable_serialized = LogeSerializer(value)
        return JsonResponse(responsable_serialized.data, safe=False)
    elif request.method == 'PUT':
        serializer = LogeSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# MEDICAMENT
@api_view(['GET', 'POST'])
def medicament_list(request):
    if request.method == 'GET':
        values = Medicament.objects.all()
        values_serialized = MedicamentSerializer(
            values, many=True)
        return JsonResponse({"medicaments": values_serialized.data}, safe=False)
    if request.method == 'POST':
        serializer = MedicamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def medicament_detail(request, id):
    try:
        value = Medicament.objects.get(pk=id)
    except Medicament.DoesNotExist:
        return JsonResponse({"error": "Le medicament n'existe pas dans la bd"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        responsable_serialized = MedicamentSerializer(value)
        return JsonResponse(responsable_serialized.data, safe=False)
    elif request.method == 'PUT':
        serializer = MedicamentSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TYPE
@api_view(['GET', 'POST'])
def type_list(request):
    if request.method == 'GET':
        values = Type.objects.all()
        values_serialized = TypeSerializer(
            values, many=True)
        return JsonResponse({"types": values_serialized.data}, safe=False)
    if request.method == 'POST':
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def type_detail(request, id):
    try:
        value = Type.objects.get(pk=id)
    except Type.DoesNotExist:
        return JsonResponse({"error": "Le type n'existe pas dans la bd"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        responsable_serialized = TypeSerializer(value)
        return JsonResponse(responsable_serialized.data, safe=False)
    elif request.method == 'PUT':
        serializer = TypeSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# APPROVISIONEMENT
@api_view(['GET', 'POST'])
def approvisionement_list(request):
    if request.method == 'GET':
        values = Approvisionement.objects.all()
        values_serialized = ApprovisionementSerializer(
            values, many=True)
        return JsonResponse({"approvisionement": values_serialized.data}, safe=False)
    if request.method == 'POST':
        serializer = AlimentationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def approvisionement_detail(request, id):
    try:
        value = Approvisionement.objects.get(pk=id)
    except Approvisionement.DoesNotExist:
        return JsonResponse({"error": "L'approvisionement n'existe pas dans la bd"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        responsable_serialized = ApprovisionementSerializer(value)
        return JsonResponse(responsable_serialized.data, safe=False)
    elif request.method == 'PUT':
        serializer = ApprovisionementSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ANIMAL
@api_view(['GET', 'POST'])
def animal_list(request):
    if request.method == 'GET':
        values = Animal.objects.all()
        values_serialized = AnimalSerializer(
            values, many=True)
        return JsonResponse({"animaux": values_serialized.data}, safe=False)
    if request.method == 'POST':
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def animal_detail(request, id):
    try:
        value = Animal.objects.get(pk=id)
    except Animal.DoesNotExist:
        return JsonResponse({"error": "L'animal n'existe pas dans la bd"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        responsable_serialized = AnimalSerializer(value)
        return JsonResponse(responsable_serialized.data, safe=False)
    elif request.method == 'PUT':
        serializer = AnimalSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ALIMENTATION
@api_view(['GET', 'POST'])
def alimentation_list(request):
    if request.method == 'GET':
        values = Alimentation.objects.all()
        values_serialized = AlimentationSerializer(
            values, many=True)
        return JsonResponse({"alimentations": values_serialized.data}, safe=False)
    if request.method == 'POST':
        serializer = AlimentationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def alimentation_detail(request, id):
    try:
        value = Alimentation.objects.get(pk=id)
    except Alimentation.DoesNotExist:
        return JsonResponse({"error": "L'aimentation n'existe pas dans la bd"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        responsable_serialized = AlimentationSerializer(value)
        return JsonResponse(responsable_serialized.data, safe=False)
    elif request.method == 'PUT':
        serializer = AlimentationSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# PRISE MEDICAMENT
@api_view(['GET', 'POST'])
def prisemedicament_list(request):
    if request.method == 'GET':
        values = Prise_medicament_animal.objects.all()
        values_serialized = Prise_medicament_animalSerializer(
            values, many=True)
        return JsonResponse({"prise_medicaments": values_serialized.data}, safe=False)
    if request.method == 'POST':
        serializer = Prise_medicament_animalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def prisemedicament_detail(request, id):
    try:
        value = Prise_medicament_animal.objects.get(pk=id)
    except Prise_medicament_animal.DoesNotExist:
        return JsonResponse({"error": "La prise medicament n'existe pas dans la bd"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        responsable_serialized = Prise_medicament_animalSerializer(value)
        return JsonResponse(responsable_serialized.data, safe=False)
    elif request.method == 'PUT':
        serializer = Prise_medicament_animalSerializer(
            value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
