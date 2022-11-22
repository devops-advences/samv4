
from odoo import models, fields



class TravelLocality(models.Model):
    _name = 'travel.locality'
    _description = 'Localité'
    _rec_name = 'name'

    code = fields.Char("Code", readonly=False, required=True)
    name = fields.Char("Nom", readonly=False, required=True)
    active = fields.Boolean("Active", default=True, required=True)

