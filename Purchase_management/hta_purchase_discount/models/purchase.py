# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    discount_amount = fields.Monetary(string='Total Remise', store=True, readonly=True, compute='_amount_discount', tracking=True)
    total_undiscount = fields.Monetary(string='Undiscount Amount', store=True, readonly=True, compute='_amount_discount', tracking=True)
    
    @api.depends('order_line.discount')
    def _amount_discount(self):
        for order in self:
            discount = 0
            undiscount = 0
            for line in order.order_line:
                discount += (line.price_unit * line.discount * line.product_qty)/100
                undiscount += line.price_unit * line.product_qty
            currency = order.currency_id or order.partner_id.property_purchase_currency_id or self.env.company.currency_id
            order.update({
                'discount_amount': currency.round(discount),
                'total_undiscount': currency.round(undiscount)
            })

    def _add_supplier_to_product(self):
        """Insert a mapping of products to PO lines to be picked up
        in supplierinfo's create()"""
        self.ensure_one()
        po_line_map = {
            line.product_id.product_tmpl_id.id: line for line in self.order_line
        }
        return super(
            PurchaseOrder, self.with_context(po_line_map=po_line_map)
        )._add_supplier_to_product()



class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    # adding discount to depends
    @api.depends("discount")
    def _compute_amount(self):
        return super()._compute_amount()

    def _prepare_compute_all_values(self):
        vals = super()._prepare_compute_all_values()
        vals.update({"price_unit": self._get_discounted_price_unit()})
        return vals

    discount = fields.Float(string="Discount (%)", digits="Discount")

    _sql_constraints = [
        (
            "discount_limit",
            "CHECK (discount <= 100.0)",
            "Discount must be lower than 100%.",
        )
    ]

    def _get_discounted_price_unit(self):
        """Inheritable method for getting the unit price after applying
        discount(s).

        :rtype: float
        :return: Unit price after discount(s).
        """
        self.ensure_one()
        if self.discount:
            return self.price_unit * (1 - self.discount / 100)
        return self.price_unit

    def _get_stock_move_price_unit(self):
        """Get correct price with discount replacing current price_unit
        value before calling super and restoring it later for assuring
        maximum inheritability.

        HACK: This is needed while https://github.com/odoo/odoo/pull/29983
        is not merged.
        """
        price_unit = False
        price = self._get_discounted_price_unit()
        if price != self.price_unit:
            # Only change value if it's different
            price_unit = self.price_unit
            self.price_unit = price
        price = super()._get_stock_move_price_unit()
        if price_unit:
            self.price_unit = price_unit
        return price

    @api.onchange("product_qty", "product_uom")
    def _onchange_quantity(self):
        """
        Check if a discount is defined into the supplier info and if so then
        apply it to the current purchase order line
        """
        res = super()._onchange_quantity()
        if self.product_id:
            date = None
            if self.order_id.date_order:
                date = self.order_id.date_order.date()
            seller = self.product_id._select_seller(
                partner_id=self.partner_id,
                quantity=self.product_qty,
                date=date,
                uom_id=self.product_uom,
            )
            self._apply_value_from_seller(seller)
        return res

    @api.model
    def _apply_value_from_seller(self, seller):
        """Overload this function to prepare other data from seller,
        like in purchase_triple_discount module"""
        if not seller:
            return
        self.discount = seller.discount

    def _prepare_account_move_line(self, move=False):
        vals = super(PurchaseOrderLine, self)._prepare_account_move_line(move)
        vals["discount"] = self.discount
        return vals

    @api.model
    def _prepare_purchase_order_line(
        self, product_id, product_qty, product_uom, company_id, supplier, po
    ):
        """Apply the discount to the created purchase order"""
        res = super()._prepare_purchase_order_line(
            product_id, product_qty, product_uom, company_id, supplier, po
        )
        partner = supplier.name
        uom_po_qty = product_uom._compute_quantity(product_qty, product_id.uom_po_id)
        seller = product_id.with_company(company_id)._select_seller(
            partner_id=partner,
            quantity=uom_po_qty,
            date=po.date_order and po.date_order.date(),
            uom_id=product_id.uom_po_id,
        )
        res.update(self._prepare_purchase_order_line_from_seller(seller))
        return res

    @api.model
    def _prepare_purchase_order_line_from_seller(self, seller):
        """Overload this function to prepare other data from seller,
        like in purchase_triple_discount module"""
        if not seller:
            return {}
        return {"discount": seller.discount}

    
    
    """@api.depends('product_qty', 'price_unit', 'taxes_id','discount')
    def _compute_amount(self):
        for line in self:
            #taxes = line.taxes_id.compute_all(line.price_unit, line.order_id.currency_id, line.product_qty, product=line.product_id, partner=line.order_id.partner_id)
            taxes = line.taxes_id.compute_all(**line._prepare_compute_all_values())
            if line.discount:
                discount = (line.price_unit * line.discount * line.product_qty)/100
                line.update({
                    'price_tax': taxes['total_included'] - taxes['total_excluded'],
                    'price_total': taxes['total_included'] ,
                    'price_subtotal': taxes['total_excluded'] - discount,
                })
            else:
                line.update({
                    'price_tax': taxes['total_included'] - taxes['total_excluded'],
                    'price_total': taxes['total_included'],
                    'price_subtotal': taxes['total_excluded'],
                })
    """