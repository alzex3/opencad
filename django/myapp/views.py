from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from services.api import get_cad_data, get_object_data

from .serializers import ParcelObjectSerializer, BuildingObjectSerializer, FlatObjectSerializer, \
    ConstructionObjectSerializer


class ObjectDataView(APIView):

    @staticmethod
    def get(request):
        cad_num = request.GET.get('cad_num')
        object_data = get_object_data(cad_num)

        if object_data.get('obj_type') == 'parcel':
            return Response(ParcelObjectSerializer(object_data).data)

        elif object_data.get('obj_type') == 'building':
            return Response(BuildingObjectSerializer(object_data).data)

        elif object_data.get('obj_type') == 'flat':
            return Response(FlatObjectSerializer(object_data).data)

        elif object_data.get('obj_type') == 'construction':
            return Response(ConstructionObjectSerializer(object_data).data)

        else:
            return Response('Rosreestr API error!')


class MainView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        search_query = request.GET.get('search_box')
        result = False
        if search_query:
            result = get_cad_data(search_query)
        context['search'] = result
        return self.render_to_response(context)
