# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (C) 2014 Sidnei Brianti scbrianti@gmail.com
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

from openerp.osv import fields, osv, orm

class res_partner(osv.osv):
    _inherit = 'res.partner'

    _columns = {
        'duration':fields.integer('Tempo de viagem (s)'),
        'distance':fields.integer('Distancia (m)')
    }
