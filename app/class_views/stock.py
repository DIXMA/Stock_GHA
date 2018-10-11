from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Product


class StockView(View):
    template_name = 'auth_templates/stock/list.html'

    def get(self, request, *args, **kwargs):

        stok = Product.objects.all()
        return render(request, self.template_name, {'stok': stok})