# -*- coding: utf-8 -*-

from urllib import request
from odoo import models, fields, api ; request


class SaleOrder(models.Model):
        _inherit='sale.order'

        date_begin=fields.Datetime("Date planifier")

        def action_confirm(self):
                task_object= request.env['project.task'].sudo().search([('id','=',self.task_id)])
                task_object.write({'planned_date_begin': self.x_date_begin})
                super(SaleOrder,self).action_confirm()


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
