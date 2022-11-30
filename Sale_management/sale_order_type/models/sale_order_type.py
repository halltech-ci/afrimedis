# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderType(models.Model):
    _name ="sale.order.type"
    _description = "Sale sequence by sale type"
    _check_company_auto = True
    
    
    @api.model
    def _get_default_domain(self):
        return [('model', '=', 'sale.order')]
    
    @api.model
    def _get_default_model(self):
        return self.env['ir.model'].search([('model', '=', 'sale.order')])
    
    name = fields.Char(required=True, translate=True)
    description = fields.Text(translate=True)
    sequence_id = fields.Many2one(comodel_name="ir.sequence", string="Entry Sequence", copy=False,)
    company_id = fields.Many2one(comodel_name="res.company", default=lambda self: self.env.company, store=True,)
    analytic_account_id = fields.Many2one(comodel_name="account.analytic.account", string="Analytic account", check_company=True,)
    #ir_model = fields.Many2one('ir.model', string="Modèle", domain=_get_default_domain, default=_get_default_model)
    active = fields.Boolean(default=True)