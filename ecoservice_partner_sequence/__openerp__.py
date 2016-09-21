# -*- coding: utf-8 -*-

# noinspection PyStatementEffect
{
    'name': 'Partner Number',
    'version': '1.0',
    'category': 'Base',
    'summary': '',
    'description': """
Adds a Sequence to res.partner
    """,
    'author': 'ecoservice',
    'website': 'https://www.ecoservice.de',
    'depends': [
        'base',
    ],
    'data': [
        'data/ir_sequence_data.xml',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
