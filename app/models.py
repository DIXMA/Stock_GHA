# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.TextField()
    nit = models.TextField(default='--', null=True, blank=True)
    city = models.CharField(max_length=200, default='--', null=True, blank=True)
    address = models.CharField(max_length=200, default='--', null=True,
                               blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    STATUS_CHOICES = ((0, 'Materia Prima'), (1, 'Inventario'), (3, 'Stock'))
    reference = models.CharField(max_length=100)
    in_mp = models.DateField(null=True, blank=True)
    caliber_mp = models.DecimalField(default=0.0, max_digits=100,
                                     decimal_places=2)
    large_mp = models.DecimalField(default=0.0, max_digits=100,
                                   decimal_places=2)
    anch_mp = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)

    price_lm = models.DecimalField(default=0.0, max_digits=100,
                                   decimal_places=2)
    price_stock = models.DecimalField(default=0.0, max_digits=100,
                                      decimal_places=2)
    state = models.CharField(max_length=30, default='Disponible')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    acabado = models.CharField(max_length=30)
    # zones
    zone_a_caliber = models.DecimalField(default=0.0, max_digits=100,
                                         decimal_places=2)
    zone_a_large = models.DecimalField(default=0.0, max_digits=100,
                                       decimal_places=2)
    zone_b_caliber = models.DecimalField(default=0.0, max_digits=100,
                                         decimal_places=2)
    zone_b_large = models.DecimalField(default=0.0, max_digits=100,
                                       decimal_places=2)
    zone_c_caliber = models.DecimalField(default=0.0, max_digits=100,
                                         decimal_places=2)
    zone_c_large = models.DecimalField(default=0.0, max_digits=100,
                                       decimal_places=2)
    zone_d_caliber = models.DecimalField(default=0.0, max_digits=100,
                                         decimal_places=2)
    zone_d_large = models.DecimalField(default=0.0, max_digits=100,
                                       decimal_places=2)
    zone_scrap_caliber = models.DecimalField(default=0.0, max_digits=100,
                                             decimal_places=2)
    zone_scrap_large = models.DecimalField(default=0.0, max_digits=100,
                                           decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StockProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    in_stock = models.DateField(null=True, blank=True)
    caliber_stock = models.DecimalField(default=0.0, max_digits=100,
                                        decimal_places=2, null=True, blank=True)
    large_stock = models.DecimalField(default=0.0, max_digits=100,
                                      decimal_places=2, null=True, blank=True)
    anch_stock = models.DecimalField(default=0.0, max_digits=100,
                                     decimal_places=2, null=True, blank=True)
    state = models.CharField(max_length=30, default='Utilizado')
    area = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TypeProductHistory(models.Model):
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
    STATE_CHOICES = ((0, 'Nnuevo'), (1, 'Iniciado'), (2, 'Finalizado'),
                     (3, 'Cancelado'))
    code = models.CharField(max_length=100, default='--', null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    init_date = models.DateField(null=True, blank=True)
    type_product = models.ForeignKey(TypeProductHistory,
                                     on_delete=models.CASCADE, null=True,
                                     blank=True)
    description = models.TextField(default='--')
    init_requirements = models.TextField(null=True, blank=True)
    init_design = models.ImageField(upload_to="uploads/project/init_design/",
                                    null=True, blank=True)
    state = models.IntegerField(choices=STATE_CHOICES, default=0)
    final_requirements = models.TextField(null=True, blank=True)
    final_design = models.ImageField(upload_to="uploads/project/final_design/",
                                     null=True, blank=True)
    materials = models.IntegerField(default=0)
    personal = models.IntegerField(default=0)
    supplies = models.IntegerField(default=0)
    sub_total = models.IntegerField(default=0)
    gain = models.IntegerField(default=0)
    pre_total = models.IntegerField(default=0)
    retention = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    risk_b = models.IntegerField(default=0)
    secure = models.IntegerField(default=0)
    commission = models.IntegerField(default=0)
    unforeseen = models.IntegerField(default=0)
    discount_opc = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Quotation(models.Model):
    STATUS_CHOICES = ((0, 'Enviada'), (1, 'Aceptada'), (2, 'Cancelada'),
                      (3, 'Terminada'),)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    price = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductsQuotation(models.Model):
    product_name = models.CharField(max_length=500, blank=True, null=True)
    product_price = models.DecimalField(max_digits=100, decimal_places=2,
                                        blank=True, null=True)
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PersonalProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    process = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    hour_price = models.IntegerField()
    hour_work = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExternalServiceProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    process = models.CharField(max_length=50)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProjectManagerMan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # Man
    date_man = models.DateField(blank=True, null=True)
    process_man = models.CharField(max_length=100, blank=True, null=True)
    init_hour_man = models.CharField(max_length=100, blank=True, null=True)
    end_hour_man = models.CharField(max_length=100, blank=True, null=True)
    total_hour_man = models.CharField(max_length=100, blank=True, null=True)
    type_employee_man = models.CharField(max_length=100, blank=True, null=True)
    price_real_man = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class ProjectManagerMachine(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # Machine
    date_mach = models.DateField(blank=True, null=True)
    process_select = models.CharField(max_length=100, blank=True, null=True)
    type_machine = models.CharField(max_length=100, blank=True, null=True)
    morning_init_time = models.CharField(max_length=100, blank=True, null=True)
    morning_end_time = models.CharField(max_length=100, blank=True, null=True)
    morning_stop_time = models.CharField(max_length=100, blank=True, null=True)
    evening_init_time = models.CharField(max_length=100, blank=True, null=True)
    evening_end_time = models.CharField(max_length=100, blank=True, null=True)
    evening_stop_time = models.CharField(max_length=100, blank=True, null=True)
    total_stop_time = models.CharField(max_length=100, blank=True, null=True)
    total_works_our = models.CharField(max_length=100, blank=True, null=True)
    total_real_works_our = models.CharField(max_length=100, blank=True,
                                            null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Role(models.Model):
    STATUS_CHOICES = ((0, 'Inactivo'), (1, 'Activo'),)
    name = models.CharField(max_length=100)
    state = models.IntegerField(choices=STATUS_CHOICES, default=1)
    description = models.CharField(max_length=255)
    objective = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
