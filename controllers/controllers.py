# -*- coding: utf-8 -*-
# from odoo import http


# class ProductLengthVariation(http.Controller):
#     @http.route('/product_length_variation/product_length_variation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_length_variation/product_length_variation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_length_variation.listing', {
#             'root': '/product_length_variation/product_length_variation',
#             'objects': http.request.env['product_length_variation.product_length_variation'].search([]),
#         })

#     @http.route('/product_length_variation/product_length_variation/objects/<model("product_length_variation.product_length_variation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_length_variation.object', {
#             'object': obj
#         })
