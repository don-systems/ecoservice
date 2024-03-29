# -*- encoding: utf-8 -*- # pylint: disable-msg=C0111
##############################################################################
#    Ecoservice Testsystem
#    Copyright (c) 2014 ecoservice GbR (<http://www.ecoservice.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    This program based on OpenERP.
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
##############################################################################
{  # pylint: disable-msg=W0104
    "name": "ecoservice: Testsystem",
    "version": "9.0.1.0",
    "depends": [],
    "author": "ecoservice",
    "website": "www.ecoservice.de",
    'summary': 'Change the Menucolor',
    "description": """Change the Menucolor""",
    "category": "Generic Modules",
    "init_xml": [],
    "update_xml": [],
    "demo_xml": [],
    'depends': ['web'],
    'data': ['views/testsystem.xml'],
    "test": [],
    "active": False,
    "installable": True
}
