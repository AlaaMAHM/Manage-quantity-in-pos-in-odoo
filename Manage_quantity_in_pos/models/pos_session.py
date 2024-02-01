from odoo import models


class PosSession(models.Model):
    """Inherited pos session for loading quantity fields from product"""
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('qty_available')
        result['search_params']['fields'].append('virtual_available')
        return result
