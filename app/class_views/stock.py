from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Product


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
        messages.success(request, "Se ha actualizado el stock correctamente")
        return redirect('stock')


class RawMaterial(View):
    template_name = "auth_templates/stock/list_raw_material.html"

    def get(self, request, *args, **kwargs):
        materials = Product.objects.filter(status=0).all()
        return render(request, self.template_name, {'materials': materials})


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
        stock = Product.objects.filter(status=1).all()
        return render(request, self.template_name, {'stock': stock})


class StrockOperatorUdateView(View):
    template_name = "auth_templates/stock/update_operator.html"

    def get(self, request, *args, **kwargs):
        materials = Product.objects.filter(status=0).all()
        return render(request, self.template_name, {'materials': materials})

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

        messages.success(request, 'Se ha sacado el material correctamente')
        return redirect('stock_operator')
