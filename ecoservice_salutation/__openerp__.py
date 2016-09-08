# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    "name": "ecoservice: Salutation",
    "version": "1.0",
    "depends": [
        "base"
    ],
    "author": "ecoservice",
    "website": "www.ecoservice.de",
    "description": """Adds a salutation for the title.""",
    "category": "Generic Modules",
    "data": [
        'sql/salutation.sql',
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
    ],
    "active": False,
    "installable": True,
}
