# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = "res.partner"
    
    def get_default_country(self):
        return self.env['res.country'].search([('code', '=', 'CI')])
    
    country_id = fields.Many2one('res.country', default=get_default_country)
    
    _sql_constraints = [
        ('ref_uniq', 'unique (ref)', 'La référence du partenaire doit être unique !')
    ]