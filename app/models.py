# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Quotation(models.Model):
    pass


class Stock(models.Model):
    ref = models.TextField()
    created_at = models.DateField()


class StockRawMaterial(models.Model):
    date_raw_material_in = models.DateField(null=True, blank=True)
    caliber = models.DecimalField(default=0.0)
