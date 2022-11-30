# -*- coding: utf-8 -*-

from odoo import models, fields, api


PURCHASE_TYPE = [('project', 'Matières/Consommables'), 
                  ('travaux', 'Travaux'), 
                  ('transport', 'Transport'), 
                  ('subcontract', 'Sous Traitance'), 
                  ('service', 'prestation de service'),
                  ('stock', 'Appro'),
                ]

class PurchaseRequest(models.Model):
    _inherit ="purchase.request"
    
    purchase_type = fields.Selection(selection = PURCHASE_TYPE, string="Type Achat", default="project")
    