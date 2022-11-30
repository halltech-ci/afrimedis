# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    agent_id = fields.Many2one(string="Apporteurs", comodel_name="res.partner", check_company=True, domain=[("agent", "=", True)])