# -*- coding: utf-8 -*-
# from odoo import http


# class Samv2Planing(http.Controller):
#     @http.route('/samv2_planing/samv2_planing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/samv2_planing/samv2_planing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('samv2_planing.listing', {
#             'root': '/samv2_planing/samv2_planing',
#             'objects': http.request.env['samv2_planing.samv2_planing'].search([]),
#         })

#     @http.route('/samv2_planing/samv2_planing/objects/<model("samv2_planing.samv2_planing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('samv2_planing.object', {
#             'object': obj
#         })
