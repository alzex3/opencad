from rest_framework import serializers

from .models import FacilityType, Facility
from services.api import get_request


class FacilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityType
        fields = [
            'name',
            'verbose_name',
        ]


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['num', 'address']

    def create(self, validated_data):
        cad_num = validated_data['num']
        i = get_request(cad_num).get(cad_num)

        Facility.objects.create(
            num=cad_num,
            type=FacilityType.objects.get(name=i.get('obj_type')),
            address=i.get('address'),
            full_address=i.get('full_address'),
            update_date=i.get('update_date'),
            created_date=i.get('created_date'),
            cost=i.get('cost'),
        )

        return i


