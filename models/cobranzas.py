from odoo import models, fields, api


class CobranzasProces(models.Model):
    _name = 'cobranzas.proces'
    _description = 'Procesos de Cobranzas'
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
    empresa = fields.Char(
        string='EMPRESA',
        required=True
    )
    datos_contrato = fields.Text(
        string='DATOS DE CONTRATO'
    )
    entidad = fields.Char(
        string='ENTIDAD'
    )
    monto_adeudado = fields.Char(
        string='MONTO ADEUDADO'
    )
    fecha_contrato = fields.Date(
        string='FECHA CONTRATO'
    )
    fecha_recepcion = fields.Date(
        string='FECHA RECEPCIÓN'
    )
    resumen_acciones = fields.Text(
        string='RESUMEN ACCIONES'
    )
    estado_proceso = fields.Text(
        string='ESTADO DEL PROCESO'
    )
    anotaciones = fields.Text(
        string='ANOTACIONES'
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('numero'):
                vals['numero'] = self.env['ir.sequence'].next_by_code('cobranzas.proces.sequence') or 0
        return super().create(vals_list)

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.numero}] {record.empresa}"
            result.append((record.id, name))
        return result
