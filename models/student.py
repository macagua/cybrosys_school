# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Student(models.Model):
    # the model name (in dot-notation, module namespace)
    _name = 'school.student'
    # python-inherited models
    _inherit = ['mail.thread']
    # the model's informal name
    _description = 'Student Record'
    # default order field for searching results
    _order = 'name'

    def button_done(self):
        for rec in self:
            rec.write({'state': 'done'})

    def button_reset(self):
        for rec in self:
            rec.state = 'reset'

    def button_cancel(self):
        for rec in self:
            rec.write({'state': 'cancel'})

    @api.depends('age')
    def _compute_level_education(self):
        # set 'level_education' using 'age'
        if self.age < 1:
            self.level_education = "kinder_garden"
        elif (self.age >= 1) and (self.age < 2):
            self.level_education = "kinder_garden"
        elif (self.age >= 2) and (self.age < 10):
            self.level_education = "primary"
        else:
            self.level_education = "secondary"

    name = fields.Char(string='Name', required=True, track_visibility=True)
    age = fields.Integer(string='Age', track_visibility=True)
    photo = fields.Binary(string='Image')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
        string='Gender')
    student_dob = fields.Date(string="Date of Birth")
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')
    level_education = fields.Selection([
        ('kinder_garden', 'Kinder Garden'),
        ('primary', 'Primary'),
        ('secondary', 'Secondary')
    ], compute="_compute_level_education")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('reset', 'Reset'),
        ('cancel', 'Cancelled'),
    ], required=True, default='draft')

