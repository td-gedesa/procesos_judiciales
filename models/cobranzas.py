from odoo import models, fields


class CobranzasProces(models.Model):
    _name = 'cobranzas.proces'
    _description = 'Procesos de Cobranzas'
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
    monto_adeudado = fields.Monetary(
        string='MONTO ADEUDADO',
        currency_field='company_currency_id'
    )
    company_currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id
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

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.numero}] {record.empresa}"
            result.append((record.id, name))
        return result
