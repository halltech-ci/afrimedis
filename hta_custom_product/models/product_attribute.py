# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Productattribute(models.Model):
    _inherit = "product.attribute"
    
    product_category = fields.Many2one('product.category')
    

class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"
    
    field_type = fields.Selection(selection=([('char', 'Alphanumeric'), ('numeric', 'Numeric')]))
    field_length = fields.Selection(selection=([('1', 'Un'), ('2', 'Deux'), ('3', 'Trois'), ('4', 'Quatre')]))
    