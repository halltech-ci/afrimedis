# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    remise_total = fields.Monetary(string='Remise Totale', store=True, readonly=True, compute='_amount_discount_no', tracking=4)
    sale_margin = fields.Float(string='Coef. Majoration (%)', default=35)
    sale_discuss_margin = fields.Float(string='Marge disc. (%)', default=0.0, copy=True)        
    note = fields.Text('Termes et conditions', default=_default_note, required=True)
    total_cost = fields.Monetary(string="Coût Total HT", compute='_compute_total_cost')#Le cout du projet
    total_margin_amount = fields.Monetary(string="Marge Brute", compute="_compute_total_margin_amount")
    total_margin_percent = fields.Float(string='Marge Brut (%)', compute='_compute_total_margin_amount')
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, change_default=True, index=True, tracking=1, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
    
        
    @api.depends('order_line.product_cost', 'order_line.product_uom_qty')
    def _compute_total_cost(self): 
        for rec in self:
            total_cost = 0
            for line in rec.order_line:
                total_cost += line.product_cost * line.product_uom_qty
            rec.total_cost = total_cost
        
    @api.depends('total_cost', 'amount_untaxed')
    def _compute_total_margin_amount(self):
        for rec in self:
            #rec.total_margin_amount = 0.0
            rec.total_margin_percent = 0.0
            rec.total_margin_amount = rec.amount_untaxed - rec.total_cost
            if rec.amount_untaxed > 0:
                rec.total_margin_percent = (1 - (rec.total_cost / rec.amount_untaxed)) * 100
    
    
    @api.onchange('amount_untaxed')
    def _onchange_amount_untaxed(self):
        for rec in self:
            #rec.total_margin_amount = 0.0
            rec.total_margin_percent = 0.0
            rec.total_margin_amount = rec.amount_untaxed - rec.total_cost
            if rec.amount_untaxed > 0:
                rec.total_margin_percent = (1 - (rec.total_cost / rec.amount_untaxed)) * 100

    @api.onchange('sale_margin')
    def _onchange_sale_margin(self):
        for line in self.order_line:
            line.line_margin = self.sale_margin
            if line.product_cost > 0:
                line.price_unit = line.product_cost * (1 + line.line_margin/100 + line.line_discuss_margin/100)
            line.line_subtotal = line.product_uom_qty * line.price_unit
            
    #amount untaxed without disc
    @api.depends('order_line.line_subtotal')
    def _amount_total_no_tax(self):
        for order in self:
            amount_no_tax = 0.0
            for line in order.order_line:
                amount_no_tax += line.line_subtotal
            order.update({
                'amount_total_no_tax': amount_no_tax
            })
    
    @api.depends('amount_total_no_tax')
    def _amount_discount_no(self):
        for order in self:
            order.remise_total = order.amount_total_no_tax - order.amount_untaxed
    
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    product_cost = fields.Float(string="Coût", digits='Product Price', copy=True)
    line_subtotal = fields.Monetary(compute='_compute_line_subtotal', string='Prix Total', readonly=True, store=True, copy=True)
    price_unit = fields.Float('Prix Unit.', required=True, digits='Product Price', compute='_compute_price_unit', store=True, copy=True)
    line_margin = fields.Float(string="Marge (%)", compute="_compute_line_margin", store=True, readonly=False, copy=True)
    line_discuss_margin = fields.Float(compute="_compute_line_margin", store=True, readonly=False, copy=True)
    
    
    @api.depends('product_cost', 'line_margin',)
    def _compute_price_unit(self):
        for line in self:
            if line.product_cost != 0:
                line.price_unit = line.product_cost * (1 + line.line_margin/100)
            if line.display_type:
                line.price_unit = 0
            else:
                continue
                            
    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        if not self.product_uom or not self.product_id:
            self.price_unit = 0.0
            return
        
        if self.order_id.pricelist_id and self.order_id.partner_id:
            product = self.product_id.with_context(
                lang=self.order_id.partner_id.lang,
                partner=self.order_id.partner_id,
                quantity=self.product_uom_qty,
                date=self.order_id.date_order,
                pricelist=self.order_id.pricelist_id.id,
                uom=self.product_uom.id,
                fiscal_position=self.env.context.get('fiscal_position')
            )
            self.price_unit = product._get_tax_included_unit_price(
                self.company_id or self.order_id.company_id,
                self.order_id.currency_id,
                self.order_id.date_order,
                'sale',
                fiscal_position=self.order_id.fiscal_position_id,
                product_price_unit=self._get_display_price(product),
                product_currency=self.currency_id
            )
        if self.product_cost > 0:
            self.price_unit = self.product_cost * (1 + self.line_margin/100 + self.line_discuss_margin/100)
        
    @api.depends("order_id", "order_id.sale_margin", "order_id.sale_discuss_margin")
    def _compute_line_margin(self):
        if hasattr(super(), "_compute_line_margin"):
            super()._compute_line_margin()
        for line in self:
            if not line.line_margin:
                line.line_margin = line.order_id.sale_margin
            if not line.line_discuss_margin:
                line.line_discuss_margin = line.order_id.sale_discuss_margin
    
    @api.depends('product_uom_qty', 'price_unit')
    def _compute_line_subtotal(self):
        for line in self:
            line.line_subtotal = line.product_uom_qty * line.price_unit
        
    @api.model
    def create(self, vals):
        """Apply sale margin for sale order lines which are not created
        from sale order form view.
        """
        if "line_margin" not in vals and "order_id" in vals:
            sale_order = self.env["sale.order"].browse(vals["order_id"])
            if sale_order.sale_margin:
                vals["line_margin"] = sale_order.sale_margin
        return super().create(vals)