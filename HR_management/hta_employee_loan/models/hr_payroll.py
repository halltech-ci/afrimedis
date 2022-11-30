# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _
from datetime import datetime
from odoo.tools import float_utils
import time
import babel


class HrPayslipInput(models.Model):
    _inherit = 'hr.payslip.input'

    loan_line_id = fields.Many2one('hr.loan.line', string="Loan Installment", help="Loan installment")
    