# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


_SALE_ORDER_DOMAINE = [('fm', ''),
                        ('cmgc', 'CONSTRUCTION METALLIQUE ET GENIE CIVIL'),
                        ('fmfe', "FABRICATION MECANIQUE ET FOURNITURE D'EQUIPEMENTS"),
                        ('mips', 'MAINTENANCE INDUSTRIELLE ET PRESTATION DE SERVICES'),
                        ('bec', "BUREAU D'ETUDE ET CONSULTANCE"),
    ]


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    
    @api.model
    def _get_sale_order_domain(self):
        domain = [('none', '')]
        sale_type = self.env['sale.order.type'].search([('active', '=', True)])
        if sale_type :
            liste = [(so.name, so.sequence_id.code) for so in sale_type]
            domain += liste
        return domain
    
    sale_order_type = fields.Selection(_SALE_ORDER_DOMAINE, string="Domaine", required=True, index=True, default='fm')
    #sale_sequence_code = fields.Char('Sale Order Sequence', compute="_get_sale_sequence_code", required = True)
            
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            next_code = "sale.order"
            domaine_code = vals.get('sale_order_type')
            if domaine_code != "fm":
                next_code = '{0}.{1}.{2}'.format('sale', domaine_code, 'sequence')
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            if 'company_id' in vals:
                #if self.company_id.name == 'CONCEPTOR INDUSTRY':
                vals['name'] = self.env['ir.sequence'].with_context(with_company=vals['company_id']).next_by_code(
                    next_code, sequence_date=seq_date) or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code(next_code, sequence_date=seq_date) or _('New')

        # Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
        if any(f not in vals for f in ['partner_invoice_id', 'partner_shipping_id', 'pricelist_id']):
            partner = self.env['res.partner'].browse(vals.get('partner_id'))
            addr = partner.address_get(['delivery', 'invoice'])
            vals['partner_invoice_id'] = vals.setdefault('partner_invoice_id', addr['invoice'])
            vals['partner_shipping_id'] = vals.setdefault('partner_shipping_id', addr['delivery'])
            vals['pricelist_id'] = vals.setdefault('pricelist_id', partner.property_product_pricelist and partner.property_product_pricelist.id)
        result = super(SaleOrder, self).create(vals)
        return result