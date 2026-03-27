from odoo import models, fields


class OtrosProces(models.Model):
    _name = 'otros.proces'
    _description = 'Procesos Judiciales Otros'
    _order = 'numero asc'

    numero = fields.Integer(
        string='Nº',
        required=True
    )
    ciudad_id = fields.Char(
        string='CIUDAD',
        required=True
    )
    tipo_proceso_id = fields.Char(
        string='TIPO',
        required=True
    )
    partes = fields.Text(
        string='PARTES'
    )
    fecha_inicio_proceso = fields.Date(
        string='FECHA INICIO PROCESO'
    )
    monto = fields.Char(
        string='MONTO'
    )
    breve_resumen = fields.Text(
        string='BREVE RESUMEN'
    )
    estado = fields.Text(
        string='ESTADO'
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
            name = f"[{record.numero}] Caso {record.numero}"
            result.append((record.id, name))
        return result
