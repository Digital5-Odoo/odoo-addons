# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 Sistemas de Datos (<http://www.sdatos.com>).
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
##############################################################################
from openerp import models, fields, api

class PickingImportWizard(models.TransientModel):
    _inherit = "picking.import.wizard"
    
    pickings = fields.Many2many(
        comodel_name='stock.picking',
        relation='distribution_import_picking_rel', column1='wizard_id',
        column2='picking_id', string='Incoming shipments',
        domain="[('partner_id', 'child_of', supplier),"
               "('location_id.usage', 'in', ['internal','supplier']),"
               "('state', '=', 'done'),"
               "('id', 'not in', prev_pickings[0][2])]", required=True)