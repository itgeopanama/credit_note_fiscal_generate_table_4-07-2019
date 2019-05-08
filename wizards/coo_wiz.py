# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)
	
class COOWiz(models.TransientModel):
	_name='coo.wiz'
	
	coo = fields.Char('COO', required=True)
	invoice_id = fields.Many2one('account.invoice')
	
	@api.multi
	def process(self):
		if self.invoice_id:
			self.invoice_id.with_context({'skip': True}).action_invoice_open()
			self.invoice_id.write({
				'coo': self.coo
			})
	