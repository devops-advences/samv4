from email.policy import default
from odoo import api, models, fields
from odoo.http import request

    


class salesInherit(models.Model):

    _inherit = 'project.task'

    driver_id = fields.Many2one('res.users')
    planned_date_begin = fields.Datetime('Date planifié')

    @api.model
    def create(self, vals):
        order = request.env['sale.order.line'].sudo().search([ ("id", "=", vals['sale_line_id'] ) ])
        date_begin = request.env['sale.order'].sudo().search([ ("id", "=", order.order_id.id ) ])
        if date_begin.x_date_begin:
            vals['planned_date_begin'] = date_begin.x_date_begin
        res_id = super(salesInherit, self).create(vals)
        return res_id





