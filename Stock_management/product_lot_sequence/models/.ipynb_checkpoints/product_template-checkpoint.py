# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    
    lot_sequence_id = fields.Many2one("ir.sequence", string="Entry Sequence", help="This field contains the information related to the numbering of lots.", copy=False,)
    lot_sequence_prefix = fields.Char(string="Sequence Prefix", help="The lot's sequence will be created using this prefix.", )
    lot_sequence_padding = fields.Integer(string="Sequence Number of Digits", default=4, help="The lots' sequence will be created using this number of digits.",)
    lot_sequence_number_next = fields.Integer(string="Next Number", help="The next sequence number will be used for the next lot.", compute="_compute_lot_seq_number_next",
                                              inverse="_inverse_lot_seq_number_next",)