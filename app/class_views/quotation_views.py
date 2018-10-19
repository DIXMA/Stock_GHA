from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Quotation, Product, Client, \
    ProductsQuotation, Project


class QuotationsView(View):
    template_name = 'auth_templates/quotations/list.html'

    def get(self, request, *args, **kwargs):

        quotations = Quotation.objects.all()
        return render(request, self.template_name, {'quotations': quotations})


class QuotationsCreateView(View):
    template_name = 'auth_templates/quotations/create.html'

    def get(self, request, pr_pk, *args, **kwargs):
        products = Product.objects.filter(state="Disponible")
        quotation = Quotation.objects.filter(project__id=pr_pk)
        project = Proje
        products_quotation = None
        if quotation:
            products_quotation = ProductsQuotation.objects.filter(quotation__id=quotation.id).all()
        return render(request, self.template_name, {'products': products, 'pr_pk': pr_pk,
                                                    'products_quotation': products_quotation,
                                                    'quotation': quotation})

    def post(self, request, *args, **kwargs):
        client = request.POST['client']
        products = request.POST.getlist('products_pk_')

        client_ = Client(name=client)
        client_.save()

        quotation = Quotation(client=client_, price=123456)
        quotation.save()

        for pr in products:
            prod = Product.objects.get(pk=pr)
            prd_q = ProductsQuotation(product=prod, quotation=quotation)
            prd_q.save

        messages.success(request, "Se ha creado la cotizacion.")

        return redirect('quotations')


class QuotationStateView(View):

    def post(self, request, *args, **kwargs):

        pk = request.POST['pk_q']
        qt = Quotation.objects.get(pk=pk)
        qt.status = request.POST['status']
        qt.save()
        messages.success(request, "Se ha actualizado el estado de la cotizacion")
        return redirect('quotations')
