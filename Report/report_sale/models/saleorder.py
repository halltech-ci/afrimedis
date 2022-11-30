# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from num2words import num2words
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    #num2words convert number to word
    def _num_to_words(self, num):
        def _num2words(number, lang):
            try:
                return num2words(number, lang=lang).title()
            except NotImplementedError:
                return num2words(number, lang='en').title()
        if num2words is None:
            logging.getLogger(__name__).warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""
        lang_code = self.env.context.get('lang') or self.env.user.lang
        lang = self.env['res.lang'].with_context(active_test=False).search([('code', '=', lang_code)])
        num_to_word = _num2words(num, lang=lang.iso_code)
        return num_to_word
        
    date_order = fields.Datetime(readonly=False)
    description = fields.Text("Description : ")
    signed_user = fields.Many2one("res.users", string="Signed In User", readonly=True, default= lambda self: self.env.uid)
    sale_order_recipient = fields.Char("Destinataire")
    amount_to_word = fields.Char(string="Montant en lettre:", compute='_compute_amount_to_word')    
    partner_code = fields.Char(string="Code Client", related="partner_id.ref")
    tax_rate = fields.Float(compute="_compute_tax_rate")
    discount_amount = fields.Monetary(string="Total Remise", compute="_compute_amount_discount", store=True)
        
    def _compute_amount_to_word(self):
        for rec in self:
            rec.amount_to_word = str(self._num_to_words(rec.amount_total)).upper()
            
    
    @api.depends('order_line.price_unit', 'order_line.product_uom_qty', 'order_line.price_subtotal')
    def _compute_amount_discount(self):
        for rec in self:
            discount = 0
            for line in rec.order_line:
                discount += line.price_unit * line.product_uom_qty - line.price_subtotal
            rec.discount_amount = discount

    
    @api.depends('order_line.tax_id')
    def _compute_tax_rate(self):
        for rec in self:
            tax = 0
            taxes = rec.order_line.tax_id
            if taxes:
                tax = taxes[0].amount
            rec.tax_rate = tax