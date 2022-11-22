# -*- coding: utf-8 -*-
from odoo import models, fields

class salesInherit(models.Model):
    _inherit = 'sale.order'

    departureplace_id = fields.Many2one('travel.locality')
    arrivalplace_id = fields.Many2one('travel.locality')


