from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Product, Project, Client, Quotation, ProductsQuotation, \
    PersonalProject, ExternalServiceProject, ProjectManagerMan, \
    TypeProductHistory, ProjectManagerMachine, StockProduct


class StockView(View):
    template_name = 'auth_templates/stock/list.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        stock = list()
        for prd in products:
            print(str(prd.id))
            prd_stk = StockProduct.objects.filter(product_id=prd.id).first()
            if prd_stk:
                prd_aux = {
                    'product': prd,
                    'stock': prd_stk
                }
            else:
                prd_aux = {
                    'product': prd,
                    'stock': ''
                }
            stock.append(prd_aux)
            print(stock)

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
        materials = Product.objects.filter(status=0).all()
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
        acabado = request.POST['acabado']

        #zones
        zone_a_caliber = request.POST['zone_a_caliber']
        zone_a_large = request.POST['zone_a_large']
        zone_b_caliber = request.POST['zone_b_caliber']
        zone_b_large = request.POST['zone_b_large']
        zone_c_caliber = request.POST['zone_c_caliber']
        zone_c_large = request.POST['zone_c_large']
        zone_d_caliber = request.POST['zone_d_caliber']
        zone_d_large = request.POST['zone_d_large']
        zone_scrap_caliber = request.POST['zone_scrap_caliber']
        zone_scrap_large = request.POST['zone_scrap_large']

        product = Product(reference=ref, in_mp=in_mp_date,
                          caliber_mp=caliber_mp, large_mp=large_mp,
                          anch_mp=anch_mp, price_lm=price, acabado=acabado,
                          zone_a_caliber=zone_a_caliber,
                          zone_a_large=zone_a_large,
                          zone_b_caliber=zone_b_caliber,
                          zone_b_large=zone_b_large,
                          zone_c_caliber=zone_c_caliber,
                          zone_c_large=zone_c_large,
                          zone_d_caliber=zone_d_caliber,
                          zone_d_large=zone_d_large,
                          zone_scrap_caliber=zone_scrap_caliber,
                          zone_scrap_large=zone_scrap_large)
        product.save()
        messages.success(request,
                         "Se ha actualizado la materia prima correctamente")
        return redirect('raw_material')


class StockOperatorView(View):
    template_name = "auth_templates/stock/list_stock_operator.html"

    def get(self, request, *args, **kwargs):
        stock = StockProduct.objects.all()
        return render(request, self.template_name, {'stock': stock})


class StrockOperatorUdateView(View):
    template_name = "auth_templates/stock/update_operator.html"

    def get(self, request, *args, **kwargs):
        materials = Product.objects.filter(status=0).all()
        return render(request, self.template_name,
                      {'materials': materials})

    def post(self, request, *args, **kwargs):
        pk = request.POST['pk']
        large_stock = request.POST['large']
        anch_stock = request.POST['anch_stock']
        in_stock = request.POST['in_stock']
        zone = request.POST['zone']
        state = request.POST['state']

        product = Product.objects.get(pk=pk)
        product.status = 3
        product.save()
        prod = StockProduct(product=product, in_stock=in_stock,
                            large_stock=large_stock, anch_stock=anch_stock,
                            state=state, area=zone)

        prod.save()

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
        types = TypeProductHistory.objects.all()
        types_arr = ''
        for tp in types:
            types_arr += str(tp.name) + ','
        return render(request, self.template_name, {'types': types_arr})

    def post(self, request, *args, **kwargs):
        try:
            code = request.POST['code']
            name_client = request.POST['name_client']
            nit_client = request.POST['nit_client']
            address_client = request.POST['address_client']
            city_client = request.POST['city_client']
            prd_type = request.POST['prd_type']
            description = request.POST['description']

            try:
                client_exist = Client.objects.get(nit=nit_client)
                client = client_exist
            except Exception:
                client = Client(name=name_client, nit=nit_client,
                                city=city_client, address=address_client)
                client.save()

            try:
                product_type = TypeProductHistory.objects.get(name=prd_type)
                type_product = product_type
            except Exception:
                type_product = TypeProductHistory(name=prd_type)
                type_product.save()

            project = Project(client=client, description=description,
                              type_product=type_product, code=code)
            project.save()
            messages.success(request, 'Se ha creado el projecto correctamente')
        except Exception:
            messages.error(request,
                           'Ha ocurrido un error interno, por favor verifique '
                           'e intentelo de nueo')
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
        return render(
            request, self.template_name, {'project': project,
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
        else:
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


class ProjectUpdateDetailsView(View):

    def post(self, request, *args, **kwargs):
        pr_pk = request.POST['pr_pk']

        try:
            project = Project.objects.get(pk=pr_pk)

            if 'init_date' in request.POST and request.POST['init_date']:
                project.init_date = request.POST['init_date']

            if 'init_requirements' in request.POST and request.POST['init_requirements']:
                project.init_requirements = request.POST['init_requirements']

            if 'final_requirements' in request.POST and request.POST['final_requirements']:
                project.final_requirements = request.POST['final_requirements']

            if 'init_design' in request.FILES and request.FILES['init_design']:
                project.init_design = request.FILES['init_design']

            if 'final_design' in request.FILES and request.FILES['final_design']:
                project.final_design = request.FILES['final_design']

            if 'per_discount' in request.POST and request.POST['per_discount']:
                project.per_discount = request.POST['per_discount']

            project.save()

            messages.success(request, 'Se han actualizado detalles al proyecto')
        except Exception as e:
            messages.error(request, 'No se reconoce la información obtenida, por favor intentelo de nuevo.')
        return redirect('projects_details', pr_pk=pr_pk)


class ProjectManagerView(View):
    template_name = "auth_templates/stock/list_project_manager.html"

    def get(self, request, pr_pk, *args, **kwargs):
        project = Project.objects.get(pk=pr_pk)
        prj_manager_man = ProjectManagerMan.objects.filter(project=project).all()
        prj_manager_machine = ProjectManagerMachine.objects.filter(project=project).all()
        return render(request, self.template_name,
                      {'prj_manager_man': prj_manager_man,
                       'prj_manager_machine': prj_manager_machine,
                       'project': project})

    def post(self, request, *args, **kwargs):
        project_pk = request.POST['pr_pk']
        type_register = request.POST['type_register']
        if type_register == 'prs':
            # MAN
            init_hour_man = request.POST['hman_init'].split(":")
            end_hour_man = request.POST['hman_end'].split(":")
            type_employee_man = request.POST['type_employee'].split(",")
            total_hour_man = int(end_hour_man[0]) - int(init_hour_man[0])
            prj_manager = ProjectManagerMan(
                project_id=project_pk, date_man=request.POST['date_prc'],
                process_man=request.POST['process_select'],
                init_hour_man=request.POST['hman_init'], end_hour_man=request.POST['hman_end'],
                total_hour_man=total_hour_man,
                type_employee_man=type_employee_man[0],
                price_real_man=int(type_employee_man[1]) * int(total_hour_man)
            )
            prj_manager.save()
            messages.success(request,
                             "Se ha agregado el registro de seguimiento "
                             "al proyecto.")
        elif type_register == 'mach':
            # MACHINE
            date_mach = request.POST['date_mach']
            process_select = request.POST['process_select']
            type_machine = request.POST['type_machine']
            morning_init_time = request.POST['morning_init_time']
            morning_end_time = request.POST['morning_end_time']
            morning_stop_time = request.POST['morning_stop_time']
            evening_init_time = request.POST['evening_init_time']
            evening_end_time = request.POST['evening_end_time']
            evening_stop_time = request.POST['evening_stop_time']
            total_works_our = request.POST['total_works_our']
            total_real_works_our = request.POST['total_real_works_our']
            total_stop_time = int(morning_stop_time) + int(evening_stop_time)

            prj_manager = ProjectManagerMachine(date_mach=date_mach,
                                                project_id=project_pk,
                                                process_select=process_select,
                                                type_machine=type_machine,
                                                morning_init_time=morning_init_time,
                                                morning_end_time=morning_end_time,
                                                morning_stop_time=morning_stop_time,
                                                evening_init_time=evening_init_time,
                                                evening_end_time=evening_end_time,
                                                evening_stop_time=evening_stop_time,
                                                total_works_our=total_works_our,
                                                total_real_works_our=total_real_works_our,
                                                total_stop_time=total_stop_time)
            prj_manager.save()
            messages.success(request,
                             "Se ha agregado el registro de seguimiento "
                             "al proyecto.")
        else:
            messages.error(request, "Se ha detectado un error en la "
                                    "información obtenida para almacenar, "
                                    "por favor verifique e intentelo de nuevo.")

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
    dic_opc = 0
    if project.per_discount:
        dic_opc = (pre_total / 100) * int(project.per_discount)
        project.discount_opc = dic_opc
    project.total = (pre_total + retention + discount + secure + commission + unforeseen) - dic_opc
    project.save()
