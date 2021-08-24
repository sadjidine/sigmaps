# -*- coding: utf-8 -*-
# from odoo import http


# class Sigmass(http.Controller):
#     @http.route('/sigmass/sigmass/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sigmass/sigmass/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sigmass.listing', {
#             'root': '/sigmass/sigmass',
#             'objects': http.request.env['sigmass.sigmass'].search([]),
#         })

#     @http.route('/sigmass/sigmass/objects/<model("sigmass.sigmass"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sigmass.object', {
#             'object': obj
#         })
