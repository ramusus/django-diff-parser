from django.views.generic.base import TemplateView
import whatthepatch


class IndexView(TemplateView):
    template_name = 'index.html'


class ParseView(TemplateView):
    template_name = 'parse.html'

    def post(self, request):
        return self.render_to_response({'diffs': whatthepatch.parse_patch(request.POST['diff'])})
