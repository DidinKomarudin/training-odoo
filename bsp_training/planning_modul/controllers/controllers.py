# -*- coding: utf-8 -*-
# from odoo import http


# class PlanningModul(http.Controller):
#     @http.route('/planning_modul/planning_modul', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/planning_modul/planning_modul/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('planning_modul.listing', {
#             'root': '/planning_modul/planning_modul',
#             'objects': http.request.env['planning_modul.planning_modul'].search([]),
#         })

#     @http.route('/planning_modul/planning_modul/objects/<model("planning_modul.planning_modul"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('planning_modul.object', {
#             'object': obj
#         })

