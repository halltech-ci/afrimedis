# -*- coding: utf-8 -*-
# from odoo import http


# class ReportSale(http.Controller):
#     @http.route('/report_sale/report_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_sale/report_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_sale.listing', {
#             'root': '/report_sale/report_sale',
#             'objects': http.request.env['report_sale.report_sale'].search([]),
#         })

#     @http.route('/report_sale/report_sale/objects/<model("report_sale.report_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_sale.object', {
#             'object': obj
#         })
