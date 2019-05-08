{
	'name': "Credit Note Fiscal Generate Details",
	'category': '',
	'author': "Onedoos",
	'website': 'https://www.onedoos.com',
	'description': """
		Generate Credit Note fiscal info in table name fiscal_header and fiscal_header for panama fiscal printer
	""",
	'depends': ['account', 'invoice_fiscal_generate_table'],
	'data': [
		'views/account_invoice_view.xml',
		'wizards/coo_wiz_view.xml',
	],
	'installable': True,
	'application': True,
}
