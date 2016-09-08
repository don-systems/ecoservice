# -*- coding: utf-8 -*-
from openerp import fields, models


class ResPartnerTitle(models.Model):
    _inherit = 'res.partner.title'
    
    salutation = fields.Char('Salutation', translate=True)
