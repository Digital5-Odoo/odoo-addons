# -*- coding: utf-8 -*-

###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Domatix (<www.domatix.com>).
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
###############################################################################

{
    'name': 'Contract Payment Mode',
    'summary': 'Payment mode in contracts and their invoices',
    'version': '8.0.1.0.0',
    'author': 'Domatix, Odoo Community Association (OCA)',
    'website': 'http://www.domatix.com',
    'depends': [
        'account_analytic_analysis',
        'account_payment_partner'],
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'data': [
        'views/contract_view.xml',
    ],
    'test': ['test/contract_payment_mode.yml'],
    'installable': True,
    'auto_install': True,
}
