from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Role


class RolesView(View):
    template_name = 'auth_templates/roles/list.html'

    def get(self, request, *args, **kwargs):
        roles = Role.objects.filter(state=1)
        return render(request, self.template_name, {'roles': roles})


class RoleCreateView(View):
    template_name = 'auth_templates/roles/create.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        desc = request.POST['description']

        role = Role(name=name, description=desc)
        role.save()

        messages.success(request, "Se ha almacenado el rol.")

        return redirect('roles')
