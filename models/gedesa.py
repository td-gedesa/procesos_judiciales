from odoo import models, fields, api


class GedresaProces(models.Model):
    _name = 'gedesa.proces'
    _description = 'Procesos Judiciales Gedesa'
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
    juzgado_nurej = fields.Char(
        string='JUZGADO/NUREJ',
        required=True
    )
    monto = fields.Char(
        string='MONTO DEMANDADO O DENUNCIADO'
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
    partes = fields.Char(
        string='Demandante / Demandado'
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('numero'):
                vals['numero'] = self.env['ir.sequence'].next_by_code('gedesa.proces.sequence') or 0
        return super().create(vals_list)

    def write(self, vals):
        return super().write(vals)

    def name_get(self):
        result = []
        for record in self:
            name = record.partes or 'N/A'
            name = f"[{record.numero}] {name}"
            result.append((record.id, name))
        return result

    def unlink(self):
        return super().unlink()
