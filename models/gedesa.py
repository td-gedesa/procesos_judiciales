from odoo import models, fields, api


class GedresaProces(models.Model):
    _name = 'gedesa.proces'
    _description = 'Procesos Judiciales Gedesa'
    _order = 'numero asc'

    numero = fields.Integer(
        string='Nº',
        required=True
    )
    ciudad_id = fields.Many2one(
        'ciudad.ciudad',
        string='CIUDAD',
        required=True
    )
    tipo_proceso = fields.Selection(
        selection=[
            ('civil', 'Civil'),
            ('laboral', 'Laboral'),
            ('mercantil', 'Mercantil'),
            ('penal', 'Penal'),
            ('administrativo', 'Administrativo'),
            ('otro', 'Otro'),
        ],
        string='TIPO DE PROCESO',
        required=True
    )
    juzgado_nurej = fields.Char(
        string='JUZGADO/NUREJ',
        required=True
    )
    demandante_o_denunciante = fields.Char(
        string='DEMANDANTE O DENUNCIANTE'
    )
    demandado_o_denunciado = fields.Char(
        string='DEMANDADO O DENUNCIADO'
    )
    monto = fields.Monetary(
        string='MONTO DEMANDADO O DENUNCIADO',
        currency_field='company_currency_id'
    )
    company_currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id
    )
    breve_resumen = fields.Text(
        string='BREVE RESUMEN DEL CASO'
    )
    estado_proceso = fields.Text(
        string='ESTADO DEL PROCESO'
    )
    proxima_actuacion_estrategia = fields.Text(
        string='PRÓXIMA ACTUACIÓN/ESTRATEGIA'
    )
    anotaciones = fields.Text(
        string='ANOTACIONES'
    )

    @api.model_create_multi
    def create(self, vals_list):
        return super().create(vals_list)

    def write(self, vals):
        return super().write(vals)

    def unlink(self):
        return super().unlink()
