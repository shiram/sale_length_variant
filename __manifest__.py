# -*- coding: utf-8 -*-
{
    'name': "sale_length_variant",

    'summary': """
        Auto Fill Product Price on Sale Order Line and Add sale by length variation.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Edward Shirambere",
    'website': "https://coderain.tech",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Products',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'sale','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': False
}
