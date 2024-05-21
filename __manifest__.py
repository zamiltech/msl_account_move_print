# -*- coding: utf-8 -*-
{
    'name': "MS Account Move Print",

    'summary': """
        -""",

    'description': """
        --
    """,

    'author': "MS",
    'website': "https://www.micro-sl.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/journal_report.xml',

    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "installable": True,    
}
