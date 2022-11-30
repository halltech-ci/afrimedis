# -*- coding: utf-8 -*-
# from odoo import http


# class ReportStock(http.Controller):
#     @http.route('/report_stock/report_stock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_stock/report_stock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_stock.listing', {
#             'root': '/report_stock/report_stock',
#             'objects': http.request.env['report_stock.report_stock'].search([]),
#         })

#     @http.route('/report_stock/report_stock/objects/<model("report_stock.report_stock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_stock.object', {
#             'object': obj
#         })
