# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderType(http.Controller):
#     @http.route('/sale_order_type/sale_order_type', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_type/sale_order_type/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_type.listing', {
#             'root': '/sale_order_type/sale_order_type',
#             'objects': http.request.env['sale_order_type.sale_order_type'].search([]),
#         })

#     @http.route('/sale_order_type/sale_order_type/objects/<model("sale_order_type.sale_order_type"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_type.object', {
#             'object': obj
#         })
