from random import randint
from odoo import _, api, fields, models

class PlanningRoleTraining(models.Model):
    _name = 'planning.role.training'
    _description = 'Planning Role Training'
    _order ='name asc'

    
    def _get_default_color(self):
        return randint(1,11)
    
    name = fields.Char('Nama Role', index=True)
    active = fields.Boolean('Active', default=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self : self.env.company)
    currency_id = fields.Many2one('res.currency', string='Currency', related='company_id.currency_id',store=True)
    point_rate = fields.Integer('Point Rate')
    amount = fields.Monetary('Amount', currency_field='currency_id')
    color = fields.Integer('Color', default=_get_default_color)
    resource_ids = fields.Many2many(comodel_name='resource.resource',
                                    relation='planning_resource_ids',
                                    column1='planning_role_id',
                                    column2='resource_id',
                                    string='Resource',
                                    domain="[('id','in', available_resources_ids)]")
    sequence = fields.Integer('Sequence')
    available_resources_ids = fields.Many2many('resource.resource',string='Available resources',compute='_compute_resource_ids')
    
   
    
    @api.depends('active')
    def _compute_resource_ids(self):
        for rec in self:
            resource_obj = self.env['resource.resource']
            if rec.active:
                uses_resources_ids = list(set(self.search([('active','=',True)]).mapped('resource_ids.id')))
                rec.available_resources_ids = resource_obj.search([('id','in',uses_resources_ids)])
            else:
                rec.available_resources_ids = resource_obj.search([])    
    
    
    
    