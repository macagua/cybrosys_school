# -*- coding: utf-8 -*-

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
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/icon.png'],
}
