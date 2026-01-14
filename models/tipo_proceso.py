from odoo import models, fields


class TipoProceso(models.Model):
    _name = 'tipo.proceso'
    _description = 'Tipo de Proceso'
    _order = 'name asc'

    name = fields.Char(
        string='Nombre del Tipo de Proceso',
        required=True,
        unique=True
    )
    codigo = fields.Char(
        string='Código',
        unique=True
    )
    description = fields.Text(
        string='Descripción'
    )
    active = fields.Boolean(
        string='Activo',
        default=True
    )

    def name_get(self):
        result = []
        for record in self:
            name = record.name
            if record.codigo:
                name = f"[{record.codigo}] {record.name}"
            result.append((record.id, name))
        return result
