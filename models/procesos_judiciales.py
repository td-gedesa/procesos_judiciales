from odoo import models, fields, api


class ProcesosJudiciales(models.Model):
    _name = 'procesos.judiciales'
    _description = 'Procesos Judiciales'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Nombre del Proceso',
        required=True,
        tracking=True
    )
    description = fields.Text(
        string='Descripción',
        tracking=True
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('active', 'Activo'),
            ('closed', 'Cerrado'),
        ],
        default='draft',
        string='Estado',
        tracking=True
    )
    date_start = fields.Date(
        string='Fecha de Inicio',
        tracking=True
    )
    date_end = fields.Date(
        string='Fecha de Fin',
        tracking=True
    )

    @api.model_create_multi
    def create(self, vals_list):
        return super().create(vals_list)

    def write(self, vals):
        return super().write(vals)

    def unlink(self):
        return super().unlink()
