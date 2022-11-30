# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    line_subtotal = fields.Monetary(string='Prix Total', readonly=True, store=True, copy=True, compute="_compute_line_subtotal")
    line_margin = fields.Float(string="Marge", store=True, readonly=False, copy=True)
    
    
    @api.onchange('line_margin')
    def _onchange_line_margin(self):
        for line in self:
            if line.purchase_price > 0:
                if line.line_margin > 0:
                    line.price_unit = line.purchase_price * (1 + line.line_margin/100)
                
        
    @api.depends('product_uom_qty', 'price_unit')
    def _compute_line_subtotal(self):
        for line in self:
            line.line_subtotal = line.product_uom_qty * line.price_unit
    
    
    