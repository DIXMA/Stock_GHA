from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Project


class LoginView(TemplateView):
    template_name = "not_aviable.html"

class LoginAction(View):

    def post(self, request, *args, **kwargs):

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Se ha iniciado sesion.')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña no validos.')
            return redirect('login')


class LogoutAction(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Se ha cerrado sesión')
        return redirect('login')


class HomeView(View):
    template_name = 'auth_templates/stock/list_projects.html'

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        return render(request, self.template_name, {'projects': projects})
