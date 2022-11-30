# -*- coding: utf-8 -*-
{
    'name': "sms_mak_hta",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mass_mailing_sms'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/mass_sms_queu.xml',
        'views/mailing_sms.xml',
        'views/views.xml',
        'views/templates.xml',
        'wizard/mailing_mailing_schedule_date_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
