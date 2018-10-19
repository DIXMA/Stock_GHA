from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import Sum

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
        project = Project.objects.get(pk=pr_pk)
        quotation = Quotation.objects.filter(project__id=pr_pk).first()
        products_quotation = None
        total = 0
        if quotation:
            products_quotation = ProductsQuotation.objects.filter(
                quotation=quotation).all()
            for prq in products_quotation:
                total += prq.total
        return render(request, self.template_name,
                      {'products': products, 'total_general': total,
                       'products_quotation': products_quotation,
                       'quotation': quotation, 'project': project})

    def post(self, request, *args, **kwargs):
        products = request.POST.getlist('products_pk_')
        total = request.POST['total_gn']
        pr_pk = request.POST['pr_pk']
        qt_pk = request.POST['qt_pk']
        if products:
            if qt_pk:
                quotation = Quotation.objects.get(pk=qt_pk)
            else:
                project = Project.objects.get(pk=pr_pk)
                quotation = Quotation(project=project, price=total)
                quotation.save()
            for pr in products:
                prd = pr.split(",")
                prod = Product.objects.get(pk=prd[0])
                prod_search = ProductsQuotation.objects.filter(
                    product__id=prod.id).count()
                if prod_search == 0:
                    prd_q = ProductsQuotation(product=prod, quotation=quotation,
                                              quantity=prd[1], total=prd[2])
                    prd_q.save()
            project.materials = total
            project.save()
            CalulcateLiquidation(project.id, project.materials,
                                 project.personal, project.supplies)
            messages.success(request, "Se ha registrado la cotizacion.")
            return redirect('projects_details', pr_pk=pr_pk)

        messages.error(request, "No se reconocen los materiales seleccionados, intentelo de nuevo.")
        return redirect('projects_quotation_create', pr_pk=pr_pk)


class QuotationStateView(View):

    def post(self, request, *args, **kwargs):

        pk = request.POST['pk_q']
        qt = Quotation.objects.get(pk=pk)
        qt.status = request.POST['status']
        qt.save()
        messages.success(request,
                         "Se ha actualizado el estado de la cotizacion")
        return redirect('quotations')


def CalulcateLiquidation(pr_pk, materials, personal, supplies):
    sub_total = int(materials) + int(personal) + int(supplies)
    gain = (sub_total / 100) * 30
    pre_total = sub_total + gain
    retention = (pre_total / 100) * 6
    discount = (pre_total / 100) * 4
    secure = (pre_total / 100) * 8
    commission = (pre_total / 100) * 3
    unforeseen = (pre_total / 100) * 2

    project = Project.objects.get(pk=pr_pk)
    project.sub_total = sub_total
    project.gain = gain
    project.pre_total = pre_total
    project.retention = retention
    project.discount = discount
    project.secure = secure
    project.commission = commission
    project.unforeseen = unforeseen
    project.save()