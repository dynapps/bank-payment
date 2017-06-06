# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2009 EduSense BV (<http://www.edusense.nl>).
#              (C) 2011 - 2013 Therp BV (<http://therp.nl>).
#              (C) 2014 ACSONE SA/NV (<http://acsone.eu>).
#
#    All other contributions are (C) by their respective contributors
#
#    All Rights Reserved
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

from odoo import api, models


class AccountPaymentLineCreate(models.TransientModel):
    _inherit = 'account.payment.line.create'

    @api.multi
    def _prepare_move_line_domain(self):
        domain = super(AccountPaymentLineCreate, self)._prepare_move_line_domain()
        if self.order_id.payment_mode_id.payment_term_ids:
            domain += [
                        ('invoice_id.payment_term_id', 'in',
                         [term.id for term in self.order_id.payment_mode_id.payment_term_ids]
                         )
                        ]
        return domain
