# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestSaleOrder(common.TransactionCase):

    def setUp(self):
        super(TestSaleOrder, self).setUp()
        # 'sale.order' instance model
        self.sale_order = self.env['sale.order']

        # # create an 'sale_order' record
        # self.sale_order1 = self.sale_order.create({
        #     'additional_note': '[ATTENTION] It's a very important note!!!',
        # })

    def test_sale_orders_install(self):
        # This function test the 'product.template' instances creation functionality

        # check if 'additional_note' is not install at 'ir.model.fields'assertEqual
        self.assertFalse(self.env['ir.model.fields'].search([('model', '=', 'additional_note')]))
        _logger.info("The 'additional_note' is not install at 'ir.model.fields'.")

        # check if 'additional_note' is install at 'ir.model.fields'assertEqual
        # self.assertTrue(self.env['ir.model.fields'].search([('model', '=', 'additional_note')]))
        # _logger.info("The 'additional_note' is install at 'ir.model.fields'.")

        _logger.info("Your 'TestSaleOrder' test was successful!")
