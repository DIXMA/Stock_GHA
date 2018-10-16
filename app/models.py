# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    STATUS_CHOICES = ((0, 'Materia Prima'), (1, 'Inventario'), (3, 'Stock'))
    reference = models.CharField(max_length=100)
    in_mp = models.DateField()
    in_inv = models.DateField()
    caliber_mp = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    caliber_inv = models.DecimalField(default=0.0, max_digits=100, decimal_places=2, null=True, blank=True)
    large_mp = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    large_inv = models.DecimalField(default=0.0, max_digits=100, decimal_places=2, null=True, blank=True)
    anch_mp = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    anch_inv = models.DecimalField(default=0.0, max_digits=100, decimal_places=2, null=True, blank=True)
    price_lm = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    price_stock = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    state = models.CharField(max_length=30)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    area = models.CharField(max_length=30)
    acabado = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Quotation(models.Model):
    STATUS_CHOICES = ((0, 'Enviada'), (1, 'Aceptada'), (2, 'Cancelada'),
                      (3, 'Terminada'),)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    price = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductsQuotation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    product_used = models.DecimalField(default=0.0, max_digits=100,
                                       decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
