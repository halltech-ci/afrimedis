# -*- coding: utf-8 -*-
# from odoo import http


# class SmsMakHta(http.Controller):
#     @http.route('/sms_mak_hta/sms_mak_hta', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sms_mak_hta/sms_mak_hta/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sms_mak_hta.listing', {
#             'root': '/sms_mak_hta/sms_mak_hta',
#             'objects': http.request.env['sms_mak_hta.sms_mak_hta'].search([]),
#         })

#     @http.route('/sms_mak_hta/sms_mak_hta/objects/<model("sms_mak_hta.sms_mak_hta"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sms_mak_hta.object', {
#             'object': obj
#         })
