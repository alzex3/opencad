from rest_framework import serializers

from .models import ObjectType, Object, ParcelObject, BuildingObject
from services.api import get_object_data

BASE_FIELDS = [
            'cad_num',
            'address',
            'obj_type',
            'update_date',
            'created_date',
            'cost', ]


class ParcelObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelObject
        fields = BASE_FIELDS + [
            'utility',
        ]


class BuildingObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingObject
        fields = BASE_FIELDS + [
            'name',
        ]


class FacilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectType
        fields = [
            'name',
            'verbose_name',
        ]


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ['cad_num', 'address']

    def create(self, validated_data):
        cad_num = validated_data['num']
        i = get_object_data(cad_num).get(cad_num)

        Object.objects.create(
            num=cad_num,
            type=ObjectType.objects.get(name=i.get('obj_type')),
            address=i.get('address'),
            full_address=i.get('full_address'),
            update_date=i.get('update_date'),
            created_date=i.get('created_date'),
            cost=i.get('cost'),
        )

        return i
