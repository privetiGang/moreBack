from rest_framework import serializers

from base.models import Dict, MetaFields, Mts, Magazine, Adidas, TypeDataSet


class DictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dict
        fields = '__all__'


class MetaFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaFields
        fields = '__all__'


class MtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mts
        fields = '__all__'


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'


class AdidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adidas
        fields = '__all__'

class TypeDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDataSet
        fields = '__all__'
