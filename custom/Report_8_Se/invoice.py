# -*- encoding: utf-8 -*-

import time
from report import report_sxw
from osv import osv
import locale

class Parser(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'time': time,
        })
