# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderType(models.Model):
    _name ="sale.order.type"
    _description = "Sale sequence by sale type"
    _check_company_auto = True
    
    
    name = fields.Char(required=True, translate=True)