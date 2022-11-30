# -*- coding: utf-8 -*-
# from odoo import http


# class HtaSaleMargin(http.Controller):
#     @http.route('/hta_sale_margin/hta_sale_margin', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_sale_margin/hta_sale_margin/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_sale_margin.listing', {
#             'root': '/hta_sale_margin/hta_sale_margin',
#             'objects': http.request.env['hta_sale_margin.hta_sale_margin'].search([]),
#         })

#     @http.route('/hta_sale_margin/hta_sale_margin/objects/<model("hta_sale_margin.hta_sale_margin"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_sale_margin.object', {
#             'object': obj
#         })
