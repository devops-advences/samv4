# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class samv2_planing(models.Model):
#     _name = 'samv2_planing.samv2_planing'
#     _description = 'samv2_planing.samv2_planing'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
