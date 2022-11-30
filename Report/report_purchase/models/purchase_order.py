# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    purchase_approver = fields.Many2one('res.users', string="Valideur")
    tax_rate = fields.Float(compute="_compute_tax_rate")
    
    @api.depends('order_line.taxes_id')
    def _compute_tax_rate(self):
        for rec in self:
            tax = 0
            taxes = rec.order_line.taxes_id
            if taxes:
                tax = taxes[0].amount
            rec.tax_rate = tax
    
    def button_approve(self, force=False):
        res = super(PurchaseOrder, self).button_approve()
        self.write({'purchase_approver' : self.env.user.id})
        return res
        