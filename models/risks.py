from odoo import api, fields, models

class RiskmanagementRisks(models.Model):
    _name = "riskmanagement.risks"
    _description = "Risk"

    risk = fields.Char(string="risk", required=True)
    inherent_risk = fields.Selection([('normal','Normal'), ('high', 'High'),('very', 'Very High')],string="Inherent risk")
    current_risk = fields.Selection([('normal','Normal'), ('high', 'High'),('very', 'Very High')],string="current risk")
    residual_risk = fields.Selection([('normal','Normal'), ('high', 'High'),('very', 'Very High')],string="Residual risk")
    department = fields.Text(string="Department")
    state_of_risk = fields.Selection([('draft','Draft'), ('approved', 'Approved')],string="State of Risk Assessment")

class RiskmanagementFramework(models.Model):
    _name = "riskmanagement.framework"
    _description = "Risk Management Database"

    prompt = fields.Char(string="prompt", required=True)
    answer = fields.Text(string="answer")
    response = fields.Text(string="response")
    