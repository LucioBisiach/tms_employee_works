# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tmsEmployeeWorks(models.Model):
    _inherit = 'hr.payslip'
    _description = 'Se agrega los trabajos realizados por empleado'

    ids_services = fields.Many2many('service.services', compute="_compute_data",string="Servicios")
    employee_tms = fields.Many2one('employee.services', string="Employee TMS")

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
