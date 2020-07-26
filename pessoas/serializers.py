from rest_framework import serializers

from pessoas.models import Pessoas


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = ('id',
                  'nome',
                  'idade')
