# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    
    partner_prefix = fields.Char('Prefix', compute="_compute_partner_prefix")
    lot_count = fields.Integer(compute="_compute_lot_count")
    lot_prefix = fields.Char('Lot Prefix', compute='_compue_lot_prefix')
    
    @api.depends('picking_id.partner_id', 'product_id')
    def _compute_lot_count(self):
        for rec in self:
            rec.lot_count = self.env['stock.move.line'].search_count([('product_id', '=', rec.product_id.id), ('picking_partner_id', '=', rec.picking_id.partner_id.id), ('lot_id', '!=', False)])        
    
    @api.depends('lot_prefix', 'lot_count', 'partner_prefix')
    def _compue_lot_prefix(self):
        date_format = datetime.today().strftime('%y%m')
        for rec in self:
            lot_num =  "%03d" % (rec.lot_count + 1)
            rec.lot_prefix = rec.partner_prefix + '/' + date_format + '/' + lot_num
    
    @api.depends('picking_partner_id')
    def _compute_partner_prefix(self):
        for rec in self:
            rec.partner_prefix = rec.picking_partner_id.ref or ''
    
    def action_generate_lot_name(self):
        self.ensure_one()
        #lot = self.env['stock.production.lot']
        prefix = self.partner_prefix
        if not self.qty_done:
            raise ValidationError(_("Veuillez indiquer la quantité recue."))
        lot_value = {
            'product_id': self.product_id.id,
            'company_id': self.company_id.id,
            'name': self.env['stock.production.lot']._get_next_serial(self.company_id, self.product_id) or self.lot_prefix + '/' + self.env['ir.sequence'].next_by_code('stock.lot.serial'),
        }
        lot = self.env['stock.production.lot'].create(lot_value)
        self.write({'lot_id' : lot.id, 'lot_name': lot.name})
        
