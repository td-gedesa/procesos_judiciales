from odoo import models, fields


class AduanaProces(models.Model):
    _name = 'aduana.proces'
    _description = 'Procesos de Aduana'
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
    empresa = fields.Char(
        string='EMPRESA',
        required=True
    )
    breve_resumen = fields.Text(
        string='BREVE RESUMEN'
    )
    fecha_inicio_proceso = fields.Date(
        string='FECHA INICIO PROCESO'
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
            name = f"[{record.numero}] {record.empresa}"
            result.append((record.id, name))
        return result
