# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sale_order_type(models.Model):
#     _name = 'sale_order_type.sale_order_type'
#     _description = 'sale_order_type.sale_order_type'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
