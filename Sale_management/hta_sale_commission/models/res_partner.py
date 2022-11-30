# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    agent_ids = fields.Many2many(comodel_name="res.partner", relation="partner_agent_rel", column1="partner_id", column2="agent_id", domain=[("agent", "=", True)], readonly=False, string="Agents",)
    # Fields for the partner when it acts as an agent
    agent = fields.Boolean(string="Creditor/Agent", help="Check this field if the partner is a creditor or an agent.", )
    agent_type = fields.Selection(selection=[("agent", "External agent")], string="Type", default="agent",)
    total_turnover = fields.Float(string="Chiffre d'affaire", compute="_compute_total_turnover", store=True, default=0.0)
    
    
    def _compute_total_turnover(self):
        for rec in self:
            moves = self.env['account.move'].search([('agent_id', '=', rec.id)])
            rec.total_turnover = sum([move.amount_untaxed for move in moves])