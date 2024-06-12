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
                                    string='Resource')
    sequence = fields.Integer('Sequence')
    
    
    
    