from django.views.generic import TemplateView

from services.api import get_cad_data


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
