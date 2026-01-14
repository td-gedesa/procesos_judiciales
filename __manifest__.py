{
    'name': 'Procesos Judiciales',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'description': 'Módulo para la gestión de procesos judiciales',
    'author': 'Alan Odoo',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
