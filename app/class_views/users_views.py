from django.views.generic import TemplateView, View


class CreateView(TemplateView):
    template_name = 'auth_templates/users/create.html'