# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseRequestApprover(http.Controller):
#     @http.route('/purchase_request_approver/purchase_request_approver', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_request_approver/purchase_request_approver/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_request_approver.listing', {
#             'root': '/purchase_request_approver/purchase_request_approver',
#             'objects': http.request.env['purchase_request_approver.purchase_request_approver'].search([]),
#         })

#     @http.route('/purchase_request_approver/purchase_request_approver/objects/<model("purchase_request_approver.purchase_request_approver"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_request_approver.object', {
#             'object': obj
#         })
