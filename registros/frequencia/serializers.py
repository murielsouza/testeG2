from rest_framework import routers, serializers, viewsets
from frequencia.models import *

class HorariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horarios
        fields = '__all__'

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    #horarios = HorariosSerializer(many= True)
    class Meta:
        model = Funcionario
        fields = '__all__'

    def create(self, validated_data):
        horarios_data = validated_data.pop('horarios')
        fun = Funcionario.objects.create(**validated_data)
        return fun

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.cpf = validated_data.get('sexo', instance.cpf)
        return instance

class FrequenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Frequencia
        fields = '__all__'

    def create(self, validated_data):
        return Frequencia.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Frequencia.objects.filter(pk=instance.pk).update(**validated_data)
        return instance

class JustificativaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Justificativa
        fields = '__all__'

    def create(self, validated_data):
        return Justificativa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Justificativa.objects.filter(pk=instance.pk).update(**validated_data)
        return instance
