from odoo import models, fields, api


class OtrosProces(models.Model):
    _name = 'otros.proces'
    _description = 'Procesos Judiciales Otros'
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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('numero'):
                vals['numero'] = self.env['ir.sequence'].next_by_code('otros.proces.sequence') or 0
        return super().create(vals_list)

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.numero}] Caso {record.numero}"
            result.append((record.id, name))
        return result
