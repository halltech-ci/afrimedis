# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    """@api.depends("order_line.agent_ids.amount")
    def _compute_commission_total(self):
        for record in self:
            record.commission_total = sum(record.mapped("order_line.agent_ids.amount"))
    """

    commission_total = fields.Float(
        string="Commissions",
        #compute="_compute_commission_total",
        store=True,
    )

    agent_id = fields.Many2one(string="Apporteurs", comodel_name="res.partner", check_company=True, domain=[("agent", "=", True)])
    
    
    def _prepare_invoice(self):
        invoice = super()._prepare_invoice()
        invoice.update({'agent_id': self.agent_id.id})
        return invoice
