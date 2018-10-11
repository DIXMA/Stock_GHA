from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Quotation, Product


class QuotationsView(View):
    template_name = 'auth_templates/quotations/list.html'

    def get(self, request, *args, **kwargs):

        quotations = Quotation.objects.all()
        return render(request, self.template_name, {'quotations': quotations})


class QuotationsCreateView(View):
    template_name = 'auth_templates/quotations/create.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(state=0)
        return render(request, self.template_name, {'products': products})

    def post(self):
        pass
