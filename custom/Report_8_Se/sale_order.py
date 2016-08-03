# -*- encoding: utf-8 -*-

import time
from report import report_sxw
from osv import osv
import locale

class Parser(report_sxw.rml_parse):

    def _amount_discount(self, sale_order):
        amount = 0.0
        for line in sale_order.order_line:
            discount = (line.discount / 100) * line.price_unit
            amount = amount + discount
        return amount

    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'time': time,
            'totalDiscount': self._amount_discount,
        })
