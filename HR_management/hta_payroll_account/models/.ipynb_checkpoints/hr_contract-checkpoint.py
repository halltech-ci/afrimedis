# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrContract(models.Model):
    _inherit = "hr.contract"
    
    account = fields.Many2one("account.account")