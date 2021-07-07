from odoo import models, fields, api


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    interviewer = fields.Char(string='Interviewer', compute='action')
    responsible = fields.Many2one('hr.employee', string='Responsible')

    gender = fields.Selection([
                ('male', 'Male'),
                ('female', 'Female'),
                ('other', 'Other')], string="Gender")
    nationality = fields.Char(string="Nationality")
    birth = fields.Date(string="Date of birth")
    address = fields.Text(string="Residential address")
    citizenship = fields.Many2one("res.country", string="Citizenship")
    marital_status = fields.Selection([
                ('married', 'Married'),
                ('widowed', 'Widowed'),
                ('divorced', 'Divorced'),
                ('never_married', 'Never Married')], string="Marital status")

    no_experience = fields.Boolean(string="No experience")
    workplace = fields.Char(string="Place of work")
    position = fields.Char(string="Position")
    work_term = fields.Integer(string="Term of work (years)")
    description = fields.Text(string="Description")

    institution = fields.Char(string="Educational institution")
    specialization = fields.Char(string="Specialization")
    date = fields.Date(string="Date of admission")
    to = fields.Date(string="Date of graduation")

    department_id = fields.Many2one('hr.department', 'Department', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    job_id = fields.Many2one('hr.job', 'Job Position', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    @api.depends('stage_id')
    def action(self):
        if self.stage_id.id >= 3:
            self.interviewer = self.department_id.manager_id
        else:
            self.interviewer = self.responsible.name
