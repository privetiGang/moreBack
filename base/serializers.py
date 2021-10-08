from rest_framework import serializers

from base.models import Dict


class DictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dict
        fields = '__all__'
