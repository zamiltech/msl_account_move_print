# -*- coding: utf-8 -*-
# from odoo import http


# class MslAccountMovePrint(http.Controller):
#     @http.route('/msl_account_move_print/msl_account_move_print', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/msl_account_move_print/msl_account_move_print/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('msl_account_move_print.listing', {
#             'root': '/msl_account_move_print/msl_account_move_print',
#             'objects': http.request.env['msl_account_move_print.msl_account_move_print'].search([]),
#         })

#     @http.route('/msl_account_move_print/msl_account_move_print/objects/<model("msl_account_move_print.msl_account_move_print"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('msl_account_move_print.object', {
#             'object': obj
#         })
