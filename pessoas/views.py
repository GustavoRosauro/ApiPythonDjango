from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from pessoas.models import Pessoas
from pessoas.serializers import PessoaSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def pessoa_list(request):
    if request.method == 'GET':
        pessoas = Pessoas.objects.all()

        nome = request.GET.get('nome', None)
        if nome is not None:
            pessoas = pessoas.filter(nome__icontains=nome)
        pessoas_serializer = PessoaSerializer(pessoas, many=True)
        return JsonResponse(pessoas_serializer.data, safe=False)
    elif request.method == 'POST':
        pessoa_data = JSONParser().parse(request)
        pessoa_serializer = PessoaSerializer(data=pessoa_data)
        if pessoa_serializer.is_valid():
            pessoa_serializer.save()
            return JsonResponse(pessoa_serializer.data, status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            count = Pessoas.objects.all().delete()
            return JsonResponse({'message': '{}  pessoas foram removidas com sucesso!'.format(count[0])},
                                status=status.HTTP_204_NO_CONTENT)
    return JsonResponse(pessoa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def pessoa_detail(request, pk):
    try:
        pessoa = Pessoas.objects.get(pk=pk)
        if request.method == 'GET':
            pessoa_serializer = PessoaSerializer(pessoa)
            return JsonResponse(pessoa_serializer.data)
        elif request.method == 'DELETE':
            pessoa.delete()
            return JsonResponse({'message': 'pessoa foi removida com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            pessoa_data = JSONParser().parse(request)
            pessoa_serializer = PessoaSerializer(pessoa, data=pessoa_data)
            if pessoa_serializer.is_valid():
                pessoa_serializer.save()
                return JsonResponse(pessoa_serializer.data)
            return JsonResponse(pessoa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Pessoas.DoesNotExist:
        return JsonResponse({'message': 'pessoa não encontrada'}, status=status.HTTP_404_NOT_FOUND)