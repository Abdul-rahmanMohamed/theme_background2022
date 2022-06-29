# Copyright (C) 2022 Abdulrahman Elsadany
{
    "name": "Theme Rebranding",
    "version": "14.0.1.0.0",
    "description""""
    change odoo logo from pos product screen into logo of company
    change shape of basic theme as whole and colors branding odoo standard
    """
    "author": "Abdulrhman Mohamed Elsadany",
    "website": "",
    "license": "AGPL-3",
    "category": "base",
    "depends": ["mail","hr_holidays",'web_enterprise','point_of_sale'],
    "data": ['views/hide_conversation_from_nav_bar.xml'],
    "qweb": [
        "static/src/xml/point_of_sale_logo.xml",
             ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
