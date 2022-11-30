# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    create_project = fields.Selection(selection=[('add_to_project', "Use project"), ('create_project', "Create Project"),], default='add_to_project')
    #project_template = fields.Many2one('project.project', string='Modele projet', domain="[('is_template', '=', True)]")
    description = fields.Text()
    
    
    def _generate_project_value(self):
        account = self.analytic_account_id
        if not account:
            self._create_analytic_account(prefix=self.description or self.name or None)
            account = self.analytic_account_id
        return {
            'name': self.client_order_ref if self.client_order_ref else self.description or self.name,
            'analytic_account_id': account.id,
            'partner_id': self.partner_id.id,
            #'sale_line_id': self.id,
            #'allow_timesheets': True,
            'sale_order_id': self.id,
            'active': True,
            'company_id': self.company_id.id,
        }
    
    def create_project_sale_confirm(self):
        values = self._generate_project_value()
        project = self.env['project.project']
        if self.create_project == "add_to_project":
            prj = self.project_id
        else:
            prj = project.create(values)
            self.write({'project_id': prj.id})
        return prj
