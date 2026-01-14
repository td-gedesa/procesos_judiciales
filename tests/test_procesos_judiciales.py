from odoo.tests import TransactionCase


class TestProcesosJudiciales(TransactionCase):
    def setUp(self):
        super().setUp()
        self.modelo = self.env['procesos.judiciales']

    def test_create_procesos_judiciales(self):
        """Test creation of a new proceso judicial"""
        proceso = self.modelo.create({
            'name': 'Test Proceso',
            'description': 'Test Description',
            'state': 'draft',
        })
        self.assertEqual(proceso.name, 'Test Proceso')
        self.assertEqual(proceso.state, 'draft')

    def test_write_procesos_judiciales(self):
        """Test update of a proceso judicial"""
        proceso = self.modelo.create({
            'name': 'Test Proceso',
            'state': 'draft',
        })
        proceso.write({
            'state': 'active'
        })
        self.assertEqual(proceso.state, 'active')

    def test_unlink_procesos_judiciales(self):
        """Test deletion of a proceso judicial"""
        proceso = self.modelo.create({
            'name': 'Test Proceso',
            'state': 'draft',
        })
        proceso_id = proceso.id
        proceso.unlink()
        self.assertFalse(self.modelo.search([('id', '=', proceso_id)]))
