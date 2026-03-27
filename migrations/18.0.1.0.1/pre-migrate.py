# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Drop foreign key constraints before converting Many2one to Char fields."""
    
    # List of tables and their foreign key columns to drop
    tables_and_columns = [
        ('gedesa_proces', 'ciudad_id'),
        ('gedesa_proces', 'tipo_proceso_id'),
        ('saint_moritz_proces', 'ciudad_id'),
        ('saint_moritz_proces', 'tipo_proceso_id'),
        ('qualitat_proces', 'ciudad_id'),
        ('qualitat_proces', 'tipo_proceso_id'),
        ('elite_brands_proces', 'ciudad_id'),
        ('elite_brands_proces', 'tipo_proceso_id'),
        ('otros_proces', 'ciudad_id'),
        ('otros_proces', 'tipo_proceso_id'),
        ('cobranzas_proces', 'ciudad_id'),
        ('aduana_proces', 'ciudad_id'),
        ('aduana_proces', 'tipo_proceso_id'),
    ]
    
    for table, column in tables_and_columns:
        # Check if table exists
        cr.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = %s
            )
        """, (table,))
        
        if not cr.fetchone()[0]:
            continue
            
        # Find and drop foreign key constraint
        cr.execute("""
            SELECT constraint_name
            FROM information_schema.table_constraints
            WHERE table_name = %s
            AND constraint_type = 'FOREIGN KEY'
            AND constraint_name LIKE %s
        """, (table, '%%%s_fkey%%' % column))
        
        for row in cr.fetchall():
            constraint_name = row[0]
            _logger.info("Dropping foreign key constraint %s on %s.%s", constraint_name, table, column)
            cr.execute(
                'ALTER TABLE "%s" DROP CONSTRAINT IF EXISTS "%s"' % (table, constraint_name)
            )
    
    _logger.info("Pre-migration completed: Foreign key constraints dropped")
