{
    "name":"Manage quantity in pos",
    "version": "16.0.1.0.0",
    "category": "Point of Sale",
    "depends": ['point_of_sale'],
    "data": ['views/res_config_settings_views.xml'],
    "image":['static/description/icon.png'],
    'assets': {
        'point_of_sale.assets': [
            '/Manage_quantity_in_pos/static/src/css/display_stock.css',
            '/Manage_quantity_in_pos/static/src/xml/ProductItem.xml',
            '/Manage_quantity_in_pos/static/src/xml/RestrictStockPopup.xml',
            '/Manage_quantity_in_pos/static/src/js/RestrictStockPopup.js',
            '/Manage_quantity_in_pos/static/src/js/ProductScreen.js',
        ],
}
}