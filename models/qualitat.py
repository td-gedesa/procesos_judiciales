from odoo import models, fields, api


class QualitatProces(models.Model):
    _name = 'qualitat.proces'
    _description = 'Procesos Judiciales Qualitat'
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
    fecha_inicio_proceso = fields.Date(
        string='FECHA INICIO PROCESO'
    )
    fecha_cierre_proceso = fields.Date(
        string='FECHA CIERRE DE PROCESO'
    )
    monto_demandado = fields.Char(
        string='MONTO DEMANDADO'
    )
    causa_demandada = fields.Text(
        string='CAUSA DEMANDADA'
    )
    monto_cancelado = fields.Char(
        string='MONTO CANCELADO'
    )
    abogado_a_cargo = fields.Char(
        string='ABOGADO A CARGO'
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
    partes = fields.Char(
        string='Demandante / Demandado'
    )

    def name_get(self):
        result = []
        for record in self:
            name = record.partes or 'N/A'
            name = f"[{record.numero}] {name}"
            result.append((record.id, name))
        return result
