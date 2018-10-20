# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.TextField()
    nit = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    STATUS_CHOICES = ((0, 'Materia Prima'), (1, 'Inventario'), (3, 'Stock'))
    reference = models.CharField(max_length=100)
    in_mp = models.DateField()
    in_inv = models.DateField(null=True, blank=True)
    caliber_mp = models.DecimalField(default=0.0, max_digits=100,
                                     decimal_places=2)
    caliber_inv = models.DecimalField(default=0.0, max_digits=100,
                                      decimal_places=2, null=True, blank=True)
    large_mp = models.DecimalField(default=0.0, max_digits=100,
                                   decimal_places=2)
    large_inv = models.DecimalField(default=0.0, max_digits=100,
                                    decimal_places=2, null=True, blank=True)
    anch_mp = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    anch_inv = models.DecimalField(default=0.0, max_digits=100,
                                   decimal_places=2, null=True, blank=True)
    price_lm = models.DecimalField(default=0.0, max_digits=100,
                                   decimal_places=2)
    price_stock = models.DecimalField(default=0.0, max_digits=100,
                                      decimal_places=2)
    state = models.CharField(max_length=30, default='Disponible')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    area = models.CharField(max_length=30)
    acabado = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
    STATE_CHOICES = ((0, 'Nnuevo'), (1, 'Iniciado'), (2, 'Finalizado'), (3, 'Cancelado'))
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    init_date = models.DateField()
    init_requirements = models.TextField()
    init_design = models.ImageField(upload_to="uploads/project/init_design/", null=True, blank=True)
    state = models.IntegerField(choices=STATE_CHOICES, default=0)
    final_requirements = models.TextField(null=True, blank=True)
    final_design = models.ImageField(upload_to="uploads/project/final_design/", null=True, blank=True)
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
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
    # Machine
    date_machine = models.DateField(blank=True, null=True)
    process_machine = models.CharField(max_length=100, blank=True, null=True)
    init_hour_machine = models.CharField(max_length=100, blank=True, null=True)
    end_hour_machine = models.CharField(max_length=100, blank=True, null=True)
    total_hour_machine = models.CharField(max_length=100, blank=True, null=True)
    price_machine = models.IntegerField(blank=True, null=True)
    price_real_machine = models.IntegerField(blank=True, null=True)
    resources_machine = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

class Role(models.Model):
    STATUS_CHOICES = ((0, 'Inactivo'), (1, 'Activo'),)
    name = models.CharField(max_length=100)
    state = models.IntegerField(choices=STATUS_CHOICES, default=1)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
