# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseRequestType(http.Controller):
#     @http.route('/purchase_request_type/purchase_request_type', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_request_type/purchase_request_type/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_request_type.listing', {
#             'root': '/purchase_request_type/purchase_request_type',
#             'objects': http.request.env['purchase_request_type.purchase_request_type'].search([]),
#         })

#     @http.route('/purchase_request_type/purchase_request_type/objects/<model("purchase_request_type.purchase_request_type"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_request_type.object', {
#             'object': obj
#         })
