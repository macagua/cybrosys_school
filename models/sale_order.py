# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleOrder(models.Model):
    # python-inherited models
    _inherit = 'sale.order'

    # new field to add to 'sale.order' model after of the 'date_order' field
    additional_note = fields.Char(string='Additional Note')

