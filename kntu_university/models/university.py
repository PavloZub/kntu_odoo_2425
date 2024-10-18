from odoo import fields, models

class UniversityClasses(models.Model):
    _name = "university.classes"
    _description = "University Classes"

    name = fields.Char(string="Name")
    learning_year = fields.Char(string="Learning Year")
    active = fields.Boolean(string="Active",default=True)
