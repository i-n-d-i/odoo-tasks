from odoo import models, fields, api


class Employee(models.Model):
    _name = 'employee.vacations'
    _description = 'manage employee vacations'

    name = fields.Char(string="Name", required=True)
    user = fields.Many2one("res.users", string="User")
    reason = fields.Text(string="Reason")
    date = fields.Date(string="From")
    to = fields.Date(string="To")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('reject', 'Rejected')], default="draft", string="Status")
    document_name = fields.Char(string="File Name")
    documents = fields.Binary(string="Employee proof")

    def action_submit(self):
        self.state = 'confirm'

    def action_reject(self):
        self.state = 'reject'