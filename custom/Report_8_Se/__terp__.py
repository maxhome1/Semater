# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Domsense s.r.l. (<http://www.domsense.com>).
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
{
    'name': 'Cantieri Casa Reports',
    'version': '0.1',
    'category': 'Generic Modules/Base',
    'description': """ Overrides standard reports  with OpenOffice reports """,
    'author': 'Domsense s.r.l.',
    'depends': ['base','report_aeroo_ooo', 'cantieri_casa_chart', 'purchase', 'l10n_it_sale', 'purchase_discount', 'sale_order_dates'],
    'update_xml': ['reports.xml'],
    'installable': True,
    'active': False,
}
