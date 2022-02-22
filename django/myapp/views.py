from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from services.api import get_cad_data, get_request

from .models import Object, ObjectType
from .serializers import FacilityTypeSerializer, FacilitySerializer, ObjectSerializer


class ObjectDataView(APIView):

    @staticmethod
    def get(request):
        cad_num = request.GET.get('cad_num')
        resp = get_request(cad_num)
        result = ObjectSerializer(resp).data
        return Response(result)


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


class FacilityTypeViewSet(ModelViewSet):
    queryset = ObjectType.objects.all()
    serializer_class = FacilityTypeSerializer


class FacilityViewSet(ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = FacilitySerializer
