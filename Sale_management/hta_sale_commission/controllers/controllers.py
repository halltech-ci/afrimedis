# -*- coding: utf-8 -*-
# from odoo import http


# class HtaSaleCommission(http.Controller):
#     @http.route('/hta_sale_commission/hta_sale_commission', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_sale_commission/hta_sale_commission/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_sale_commission.listing', {
#             'root': '/hta_sale_commission/hta_sale_commission',
#             'objects': http.request.env['hta_sale_commission.hta_sale_commission'].search([]),
#         })

#     @http.route('/hta_sale_commission/hta_sale_commission/objects/<model("hta_sale_commission.hta_sale_commission"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_sale_commission.object', {
#             'object': obj
#         })
