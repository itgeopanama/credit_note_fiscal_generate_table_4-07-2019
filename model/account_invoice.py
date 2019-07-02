# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
import logging
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
import json

_logger = logging.getLogger(__name__)
	
class AccountInvoice(models.Model):
	_inherit='account.invoice'
	
	coo = fields.Char('COO')
	
	@api.multi
	def write(self, vals):
		if vals.get('coo') and self.type in ['out_refund']:
			self.fiscal_header.write({'coo': vals.get('coo')})
			
		return super(AccountInvoice, self).write(vals)
		
	@api.multi
	def action_invoice_open(self):
		_logger.info(self._context)
		_logger.info(self.type)
		if self._context.get('skip') or self.type not in ['out_refund']:
			return super(AccountInvoice, self).action_invoice_open()
		else:
			dummy, view_id = self.env['ir.model.data'].get_object_reference('credit_note_fiscal_generate_table', 'coo_wiz_form_view')
			for inv in self:
				return {
					'name': _("Add COO"),
					'view_mode': 'form',
					'view_id': view_id,
					'res_model': 'coo.wiz',
					'type': 'ir.actions.act_window',
					'target': 'new',
					'domain': '[]',
					'context': {
						'default_invoice_id': inv.id,
					}
				}
		
class FiscalHeader(models.Model):
	_inherit="fiscal.header"
	
	coo = fields.Char('COO')
	
