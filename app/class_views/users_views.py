from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

from app.models import Employee, Role


class UsersCreateView(View):
    template_name = 'auth_templates/users/create.html'

    def get(self, request, *args, **kwargs):
        roles = Role.objects.filter(state=1).all()
        return render(request, self.template_name, {'roles': roles})

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        lastname = request.POST['lastname']
        password = request.POST['password']
        email = request.POST['email']
        rol = request.POST['role']

        user = User(first_name=name, last_name=lastname, username=email, email=email, password=password)
        user.save()
        employee = Employee(user=user, role_id=rol)
        employee.save()
        messages.success(request, "Se ha registado el nuevo empleado, ahora podra iniciar sesion en el sistema.")
        return redirect('users')


class UsersListView(View):
    template_name = 'auth_templates/users/list.html'

    def get(self, request, *args, **kwargs):
        employes = Employee.objects.all()
        return render(request, self.template_name, {'employees': employes})

    def post(self, request, *args, **kwargs):
        pk = request.POST['user_id']
        emp = Employee.objects.get(pk=pk)
        emp.delete()
        messages.success(request, "Se ha eliminado el usuario")
        return redirect('users')
