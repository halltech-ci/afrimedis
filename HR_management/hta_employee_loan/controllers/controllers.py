# -*- coding: utf-8 -*-
# from odoo import http


# class HtaEmployeeLoan(http.Controller):
#     @http.route('/hta_employee_loan/hta_employee_loan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_employee_loan/hta_employee_loan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_employee_loan.listing', {
#             'root': '/hta_employee_loan/hta_employee_loan',
#             'objects': http.request.env['hta_employee_loan.hta_employee_loan'].search([]),
#         })

#     @http.route('/hta_employee_loan/hta_employee_loan/objects/<model("hta_employee_loan.hta_employee_loan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_employee_loan.object', {
#             'object': obj
#         })
