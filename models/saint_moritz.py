from odoo import models, fields


class SaintMoritzProces(models.Model):
    _name = 'saint.moritz.proces'
    _description = 'Procesos Judiciales Saint Moritz'
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
    tipo_proceso_id = fields.Many2one(
        'tipo.proceso',
        string='TIPO DE PROCESO',
        required=True
    )
    juzgado_nurej = fields.Char(
        string='JUZGADO/NUREJ',
        required=True
    )
    demandante_o_denunciante = fields.Char(
        string='DEMANDANTE'
    )
    demandado_o_denunciado = fields.Char(
        string='DEMANDADO'
    )
    fecha_inicio_proceso = fields.Date(
        string='FECHA INICIO PROCESO'
    )
    monto_demandado = fields.Monetary(
        string='MONTO DEMANDADO',
        currency_field='company_currency_id'
    )
    company_currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id
    )
    causa_demandada = fields.Text(
        string='CAUSA DEMANDADA'
    )
    monto_cancelado = fields.Monetary(
        string='MONTO CANCELADO',
        currency_field='company_currency_id'
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

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.numero}] {record.demandante_o_denunciante or 'N/A'}"
            result.append((record.id, name))
        return result
