from rest_framework import serializers

from base.models import Dict, MetaFields, Mts, Magazine


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
