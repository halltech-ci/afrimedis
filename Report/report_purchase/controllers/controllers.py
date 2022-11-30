# -*- coding: utf-8 -*-
# from odoo import http


# class ReportPurchase(http.Controller):
#     @http.route('/report_purchase/report_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_purchase/report_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_purchase.listing', {
#             'root': '/report_purchase/report_purchase',
#             'objects': http.request.env['report_purchase.report_purchase'].search([]),
#         })

#     @http.route('/report_purchase/report_purchase/objects/<model("report_purchase.report_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_purchase.object', {
#             'object': obj
#         })
