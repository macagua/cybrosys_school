# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'School',
    'version': '13.0.0.0.1',
    'summary': 'Record Student Information',
    'description': '',
    'category': 'Tools',
    'author': 'Niyas Raphy',
    'maintainer': "Leonardo J. Caballero G.",
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'license': 'AGPL-3',
    'depends': ['base', 'mail', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/student_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}

