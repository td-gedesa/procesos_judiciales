from odoo import models, fields, api


class AduanaProces(models.Model):
    _name = 'aduana.proces'
    _description = 'Procesos de Aduana'
    _order = 'numero asc'

    numero = fields.Integer(
        string='Nº',
        readonly=True,
        copy=False
    )
    ciudad_id = fields.Char(
        string='CIUDAD',
        required=True
    )
    tipo_proceso_id = fields.Char(
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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('numero'):
                vals['numero'] = self.env['ir.sequence'].next_by_code('aduana.proces.sequence') or 0
        return super().create(vals_list)

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.numero}] {record.empresa}"
            result.append((record.id, name))
        return result
