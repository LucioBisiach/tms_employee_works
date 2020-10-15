# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class tmsEmployeeWorks(models.Model):
    _inherit = 'hr.payslip'
    _description = 'Se agrega los trabajos realizados por empleado'

    ids_services = fields.Many2many('service.services', compute="_compute_data",string="Servicios")
    employee_tms = fields.Many2one('employee.services', string="Employee TMS")

    qty_viatico_comida = fields.Float(string="Comida")
    qty_viatico_especial = fields.Float(string="V. Especial")
    qty_viatico_km = fields.Float(string="Km")
    qty_viatico_ccyd = fields.Float(string="CCyD")
    qty_viatico_km_he = fields.Float(string="KM H.E.")
    qty_viatico_he = fields.Float(string="H.E.")

    @api.depends('date_from', 'date_to', 'employee_tms')
    def _compute_data(self):
        # Definimos el dominio con el cual queremos filtrar los datos que vamos a traer de la clase service.services
        servicios_domain = [
            ('employee', 'in', self.employee_tms.ids),
            ('date_start', '>=', self.date_from),
            ('date_start', '<=', self.date_to),
        ]
        # Traemos los servicios de dicha clase y los ordenamos por los valores que querramos, en caso de querer ordenar por mas valores, seguir con una coma ingresar el campo y el orden
        servicios = self.env['service.services'].search(servicios_domain, order='date_start asc')
        self.ids_services = servicios


    def get_viaticos(self):
        self.qty_viatico_comida = 0
        self.qty_viatico_especial = 0
        self.qty_viatico_km = 0
        self.qty_viatico_ccyd = 0
        self.qty_viatico_km_he = 0
        self.qty_viatico_he = 0
        if len(self.ids_services) == 0:
            _logger.info("No hay servicios")
            self.qty_viatico_comida = 0
            self.qty_viatico_especial = 0
            self.qty_viatico_km = 0
        else:
            _logger.info("Hay servicios")
            for obj in self.ids_services:
                for costos in obj.costos_ids:
                    if costos.employee.ids == self.employee_tms.ids:
                        _logger.info("El costo es: %s", costos.name.name)
                        if costos.name.code == '4.1.12':
                            self.qty_viatico_comida += costos.qty
                        if costos.name.code == '4.1.13':
                            self.qty_viatico_especial += costos.qty
                        if costos.name.code == '4.2.14':
                            self.qty_viatico_he += costos.qty
                        if costos.name.code == '4.2.4':
                            self.qty_viatico_km += costos.qty
                        if costos.name.code == '4.2.3':
                            self.qty_viatico_km_he += costos.qty
                        if costos.name.code == '4.2.6':
                            self.qty_viatico_ccyd += costos.qty