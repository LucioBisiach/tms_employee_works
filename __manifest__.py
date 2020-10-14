# -*- coding: utf-8 -*-
{
    'name': "Payroll employee work's",

    'summary': """
        """,

    'description': """
        Se agrega una pestaña de los servicios realizados 
    """,

    'author': "Bisiach Lucio",
    'website': "http://www.bisiachlucio.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'transport_manager', 'om_hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
