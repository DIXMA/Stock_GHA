from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Role, Employee


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


class RolDeactivateView(View):

    def post(self, request, *args, **kwargs):
        try:
            uuid = request.POST['uuid']
            if uuid:
                rol = Role.objects.get(pk=uuid)
                users = Employee.objects.filter(role=rol.id)
                if users:
                    messages.warning(request, "El rol ya se ha asignado a usuarios.")
                else:
                    rol.state = 0
                    rol.save()
                    messages.success(request, "Se ha eliminado el rol.")
                    messages.warning(request, "El rol ya se ha asignado a usuarios.")
                return redirect('roles')
        except:
            print("Error interno")
