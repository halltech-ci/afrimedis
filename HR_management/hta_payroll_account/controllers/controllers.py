# -*- coding: utf-8 -*-
# from odoo import http


# class HtaPayrollAccount(http.Controller):
#     @http.route('/hta_payroll_account/hta_payroll_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_payroll_account/hta_payroll_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_payroll_account.listing', {
#             'root': '/hta_payroll_account/hta_payroll_account',
#             'objects': http.request.env['hta_payroll_account.hta_payroll_account'].search([]),
#         })

#     @http.route('/hta_payroll_account/hta_payroll_account/objects/<model("hta_payroll_account.hta_payroll_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_payroll_account.object', {
#             'object': obj
#         })
