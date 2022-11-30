# -*- coding: utf-8 -*-
# from odoo import http


# class HtaPurchaseDiscount(http.Controller):
#     @http.route('/hta_purchase_discount/hta_purchase_discount', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_purchase_discount/hta_purchase_discount/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_purchase_discount.listing', {
#             'root': '/hta_purchase_discount/hta_purchase_discount',
#             'objects': http.request.env['hta_purchase_discount.hta_purchase_discount'].search([]),
#         })

#     @http.route('/hta_purchase_discount/hta_purchase_discount/objects/<model("hta_purchase_discount.hta_purchase_discount"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_purchase_discount.object', {
#             'object': obj
#         })
