# -*- encoding: utf-8 -*-
##############################################################################
#    Ecoservice Partner
#    Copyright (c) 2013 ecoservice GbR (<http://www.ecoservice.de>).
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
{   # pylint: disable-msg=W0104
    'name': 'ecoservice: Task Color', # pylint: disable-msg=W0311
    'version': '7.0.0.1',
    'depends': ['project'],
    'author': 'ecoservice',
	'data' : [],
    'website': 'http://www.ecoservice.de',
    'summary': 'Color setting for project',
    'description': """Color setting for each project . Each task of the project has the same color.

Further information under
* https://www.ecoservice.de/
* https://www.ecoservice.de/event

""",
    'category': 'Project Management',
    'installable': True
}
