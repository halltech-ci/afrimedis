from odoo import models, fields, api


class purchase_custom(models.Model):
    _inherit = 'purchase.order'
#     _description = 'purchase_custom.purchase_custom'

    authorized_by = fields.Many2one('res.users', string="Autorisé par")
