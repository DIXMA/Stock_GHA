from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Product, Project, Client, Quotation, ProductsQuotation, \
    PersonalProject, ExternalServiceProject, ProjectManagerMan


class StockView(View):
    template_name = 'auth_templates/stock/list.html'

    def get(self, request, *args, **kwargs):
        stock = Product.objects.all()
        return render(request, self.template_name, {'stock': stock})


class StockCreateView(View):
    template_name = "auth_templates/stock/register.html"

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        ref = request.POST['ref']
        in_mp_date = request.POST['in_mp_date']
        caliber_mp = request.POST['caliber_mp']
        large_mp = request.POST['large_mp']
        anch_mp = request.POST['anch_mp']
        price = request.POST['price']
        in_inv_date = request.POST['in_inv_date']
        caliber_inv = request.POST['caliber_inv']
        large_inv = request.POST['large_inv']
        anch_inv = request.POST['anch_inv']
        acb = request.POST['acb']
        area = request.POST['area']
        disp = request.POST['disp']
        price_stock = request.POST['price_stock']

        product = Product(reference=ref,
                          in_mp=in_mp_date,
                          in_inv=in_inv_date,
                          caliber_mp=caliber_mp,
                          caliber_inv=caliber_inv,
                          large_mp=large_mp,
                          large_inv=large_inv,
                          anch_mp=anch_mp,
                          anch_inv=anch_inv,
                          price_lm=price,
                          price_stock=price_stock,
                          area=area,
                          acabado=acb,
                          state=disp)
        product.save()
        messages.success(request,
                         "Se ha actualizado el stock correctamente")
        return redirect('stock')


class RawMaterial(View):
    template_name = "auth_templates/stock/list_raw_material.html"

    def get(self, request, *args, **kwargs):
        materials = Product.objects.all()
        return render(request, self.template_name,
                      {'materials': materials})


class RawMaterialCreateView(View):
    template_name = "auth_templates/stock/create_raw_material.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        ref = request.POST['ref']
        in_mp_date = request.POST['in_mp_date']
        caliber_mp = request.POST['caliber_mp']
        large_mp = request.POST['large_mp']
        anch_mp = request.POST['anch_mp']
        price = request.POST['price']

        product = Product(reference=ref, in_mp=in_mp_date,
                          caliber_mp=caliber_mp, large_mp=large_mp,
                          anch_mp=anch_mp, price_lm=price)
        product.save()
        messages.success(request,
                         "Se ha actualizado la materia prima correctamente")
        return redirect('raw_material')


class StockOperatorView(View):
    template_name = "auth_templates/stock/list_stock_operator.html"

    def get(self, request, *args, **kwargs):
        stock = Product.objects.all()
        return render(request, self.template_name, {'stock': stock})


class StrockOperatorUdateView(View):
    template_name = "auth_templates/stock/update_operator.html"

    def get(self, request, *args, **kwargs):
        materials = Product.objects.filter(status=0).all()
        return render(request, self.template_name,
                      {'materials': materials})

    def post(self, request, *args, **kwargs):
        pk = request.POST['pk']
        caliber = request.POST['caliber']
        large = request.POST['large']
        ancho = request.POST['ancho']
        acabado = request.POST['acabado']
        area = request.POST['area']
        date = request.POST['date']
        state = request.POST['state']

        product = Product.objects.get(pk=pk)
        product.caliber_inv = caliber
        product.large_inv = large
        product.anch_inv = ancho
        product.state = state
        product.area = area
        product.acabado = acabado
        product.in_inv = date
        product.status = 1

        product.save()

        messages.success(request,
                         'Se ha sacado el material correctamente')
        return redirect('stock_operator')


class ProjectsView(View):
    template_name = "auth_templates/stock/list_projects.html"

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        return render(request, self.template_name, {'projects': projects})


class ProjectCreateView(View):
    template_name = "auth_templates/stock/create_projects.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        name_client = request.POST['name_client']
        nit_client = request.POST['nit_client']
        init_date = request.POST['init_date']
        design = request.FILES['design']
        requirements = request.POST['requirements']

        client = Client(name=name_client, nit=nit_client)
        client.save()

        project = Project(client=client, init_date=init_date,
                          init_requirements=requirements,
                          init_design=design)
        project.save()
        messages.success(request, 'Se ha creado el projecto correctamente')
        return redirect('projects')


class ProjectDetailsView(View):
    template_name = "auth_templates/stock/show_project.html"

    def get(self, request, pr_pk, *args, **kwargs):
        project = Project.objects.get(pk=pr_pk)
        quotation = Quotation.objects.filter(project__id=project.id).first()
        products_quotation = None
        if quotation:
            products_quotation = ProductsQuotation.objects.filter(
                quotation__id=quotation.id).all()
        personal_project = PersonalProject.objects.filter(
            project__id=project.id).all()
        external_services = ExternalServiceProject.objects.filter(
            project__id=project.id).all()
        return render(request, self.template_name, {'project': project,
                                                    'quotation': quotation,
                                                    'products_quotation': products_quotation,
                                                    'personal_project': personal_project,
                                                    'external_services': external_services})


class ProjectPersonalCreate(View):
    template_name = "auth_templates/stock/create_personal_project.html"

    def get(self, request, pr_pk, *args, **kwargs):
        project = Project.objects.get(pk=pr_pk)
        prs_project = PersonalProject.objects.filter(project=project).all()
        total_general = 0
        if prs_project:
            for prx in prs_project:
                total_general += prx.total_price
        return render(request, self.template_name, {'project': project,
                                                    'prs_project': prs_project,
                                                    'total_general': total_general})

    def post(self, request, *args, **kwargs):

        pr_pk = request.POST['pr_pk']
        personals = request.POST.getlist('prs_pk_')
        total_gn = request.POST['total_gn']

        if personals:
            project = Project.objects.get(pk=pr_pk)
            for pr in personals:
                prs = pr.split(',')
                prs_search = PersonalProject.objects.filter(project=project,
                                                            process=prs[
                                                                0]).count()
                if prs_search == 0:
                    personal = PersonalProject(project=project, process=prs[0],
                                               specialty=prs[1],
                                               hour_price=prs[2],
                                               hour_work=prs[3],
                                               total_price=prs[4])
                    personal.save()

            project.personal = total_gn
            project.save()

            CalulcateLiquidation(project.id, project.materials,
                                 project.personal, project.supplies)

            messages.success(request, "Se ha registrado el personal.")
            return redirect('project_personal', pr_pk=pr_pk)

        messages.error(request,
                       "No se puede guardar el personal en el proyecto")
        return redirect('projects_details', pr_pk=pr_pk)


class ProjectExternalServicesVew(View):
    template_name = "auth_templates/stock/create_services_project.html"

    def get(self, request, pr_pk, *args, **kwargs):
        project = Project.objects.get(pk=pr_pk)
        ex_services = ExternalServiceProject.objects.filter(
            project=project).all()
        total = 0
        if ex_services:
            for exs in ex_services:
                total += exs.total_price
        return render(request, self.template_name, {'project': project,
                                                    'ex_services': ex_services,
                                                    'total_general': total})

    def post(self, request, *args, **kwargs):

        pr_pk = request.POST['pr_pk']
        total_gn = request.POST['total_gn']
        exs_pk_ = request.POST.getlist('exs_pk_')

        if exs_pk_:
            project = Project.objects.get(pk=pr_pk)
            for exs in exs_pk_:
                external = exs.split(',')
                extra = ExternalServiceProject(project=project,
                                               process=external[0],
                                               unit_price=external[1],
                                               quantity=external[2],
                                               total_price=external[3])
                extra.save()

            project.supplies = total_gn
            project.save()
            CalulcateLiquidation(project.id, project.materials,
                                 project.personal, project.supplies)
            messages.success(request, "Se ha agregado correctamente")
            return redirect('projects_details', pr_pk=pr_pk)

        messages.error(request,
                       "No se reconoce la informacion, intentelo de nuevo")
        return redirect('project_external_services', pr_pk=pr_pk)


class ProjectUpdateStateView(View):

    def post(self, request, *args, **kwargs):
        pr_pk = request.POST['pr_pk']
        state = request.POST['state']
        project = Project.objects.get(pk=pr_pk)
        project.state = state
        project.save()
        messages.success(request, 'Se ha actualizado el estado del proyecto')
        return redirect('projects_details', pr_pk=pr_pk)


class ProjectManagerView(View):
    template_name = "auth_templates/stock/list_project_manager.html"

    def get(self, request, pr_pk, *args, **kwargs):
        project = Project.objects.get(pk=pr_pk)
        prj_manager = ProjectManagerMan.objects.filter(project=project).all()
        return render(request, self.template_name, {'prj_manager': prj_manager,
                                                    'project': project})

    def post(self, request, *args, **kwargs):
        project_pk = request.POST['pr_pk']
        date_man = request.POST['date_prc']
        process_man = request.POST['process_select']
        # MAN
        init_hour_man = request.POST['hman_init']
        end_hour_man = request.POST['hman_end']
        total_hour_man = request.POST['hman_tot']
        type_employee_man = request.POST['type_employee']
        price_real_man = request.POST['price_mo']
        # MACHINE
        init_hour_machine = request.POST['hmaq_init']
        end_hour_machine = request.POST['hmaq_end']
        total_hour_machine = request.POST['hmaq_tot']
        price_machine = request.POST['price_mqh']
        price_real_machine = request.POST['price_ma']
        resources_machine = request.POST['resources']

        prj_manager = ProjectManagerMan(
            project_id=project_pk, date_man=date_man, process_man=process_man,
            init_hour_man=init_hour_man, end_hour_man=end_hour_man,
            total_hour_man=total_hour_man, type_employee_man=type_employee_man,
            price_real_man=price_real_man, init_hour_machine=init_hour_machine,
            end_hour_machine=end_hour_machine, price_machine=price_machine,
            total_hour_machine=total_hour_machine,
            price_real_machine=price_real_machine,
            resources_machine=resources_machine
        )
        prj_manager.save()
        messages.success(request, "Se ha agregado el registro de seguimiento "
                                  "al proyecto.")
        return redirect('project_manager', pr_pk=project_pk)


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
