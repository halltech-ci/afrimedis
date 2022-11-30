# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Settlement(models.Model):
    _name = "sale.commission.settlement"
    _description = "Settlement"
    
    
    agent_id = fields.Many2one(
        comodel_name="res.partner", domain="[('agent', '=', True)]"
    )