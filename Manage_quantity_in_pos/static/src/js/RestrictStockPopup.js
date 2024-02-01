/** @odoo-module **/
/*
 * This file is used to store a popup for stocks out of stock for forced orders.
 */
import AbstractAwaitablePopup from 'point_of_sale.AbstractAwaitablePopup';
import Registries from 'point_of_sale.Registries';

class RestrictStockPopup extends AbstractAwaitablePopup {
    _OrderProduct() {
        var product = this.env.pos.db.get_product_by_id(this.props.pro_id)
        this.cancel();
    }
}
RestrictStockPopup.template = 'RestrictStockPopup';
Registries.Component.add(RestrictStockPopup);
