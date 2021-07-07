# -*- coding: utf-8 -*-
# from odoo import http


# class Second-project-2(http.Controller):
#     @http.route('/second-project-2/second-project-2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/second-project-2/second-project-2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('second-project-2.listing', {
#             'root': '/second-project-2/second-project-2',
#             'objects': http.request.env['second-project-2.second-project-2'].search([]),
#         })

#     @http.route('/second-project-2/second-project-2/objects/<model("second-project-2.second-project-2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('second-project-2.object', {
#             'object': obj
#         })
