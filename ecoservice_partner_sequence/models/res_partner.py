# -*- coding: utf-8 -*-

from openerp import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    supplier_ref = fields.Char(string='Supplier Reference')

    def reset_sequencenumber(self, cr, uid, context=None):
        # Customer
        sequence = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'ecoservice_partner_sequence', 'ecoservice_companycode')
        if sequence:
            self.pool.get(sequence[0]).write(cr, uid, [sequence[1]], {'number_next_actual': 1})

        # Supplier
        supplier_sequence = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'ecoservice_partner_sequence', 'ecoservice_companycode_supplier')
        if supplier_sequence:
            self.pool.get(supplier_sequence[0]).write(cr, uid, [supplier_sequence[1]], {'number_next_actual': 1})
        return True

    @api.model
    def create(self, values):
        if values.get('is_company', False):
            # Customer Reference
            if 'customer' in values and values['customer']:
                if not values.get('ref', False):
                    values['ref'] = self.with_context(is_company=True).create_customer_reference()

            # Supplier Reference
            if 'supplier' in values and values['supplier']:
                if not values.get('supplier_ref', False):
                    values['supplier_ref'] = self.with_context(is_company=True).create_supplier_reference()
        return super(ResPartner, self).create(values)

    def button_create_ref(self, res_id, val):
        self = res_id or self
        if self.is_company and val:
            if val == 'customer' and self.customer:
                self.ref = self.with_context(is_company=True).create_customer_reference()

            # Supplier Reference
            if val == 'supplier' and self.supplier:
                self.supplier_ref = self.with_context(is_company=True).create_supplier_reference()
        return True

    def create_customer_reference(self):
        ref = False
        if self.is_company or self._context.get('is_company', False):
            sequence = self.env['ir.model.data'].get_object_reference('ecoservice_partner_sequence', 'ecoservice_companycode')
            if sequence:
                seq = self.env['ir.sequence'].browse(sequence[1])
                ref = seq.next_by_id()
        return ref

    def create_supplier_reference(self):
        supplier_ref = False
        if self.is_company or self._context.get('is_company', False):
            supplier_sequence = self.env['ir.model.data'].get_object_reference('ecoservice_partner_sequence', 'ecoservice_companycode_supplier')
            if supplier_sequence:
                supplier_seq = self.env['ir.sequence'].browse(supplier_sequence[1])
                supplier_ref = supplier_seq.next_by_id()
        return supplier_ref
