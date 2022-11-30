# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrSalaryRule(models.Model):
    _inherit="hr.salary.rule"
    
    input_ids = fields.One2many('hr.salary.rule.input', 'input_id', string='Inputs', copy=True)


class HrSalaryRuleInput(models.Model):
    _name = 'hr.salary.rule.input'
    _description = 'Salary Rule Input'

    name = fields.Char(string='Description', required=True)
    code = fields.Char(required=True, help="The code that can be used in the salary rules")
    input_id = fields.Many2one('hr.salary.rule', string='Salary Rule Input', required=True)
