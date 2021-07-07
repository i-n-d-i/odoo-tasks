# -*- coding: utf-8 -*-
# from odoo import http


# class First-project(http.Controller):
#     @http.route('/first-project/first-project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/first-project/first-project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('first-project.listing', {
#             'root': '/first-project/first-project',
#             'objects': http.request.env['first-project.first-project'].search([]),
#         })

#     @http.route('/first-project/first-project/objects/<model("first-project.first-project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('first-project.object', {
#             'object': obj
#         })
