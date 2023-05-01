from odoo import models, fields, api


class TrustSales(models.Model):
    _inherit = 'sale.order'
    trust = fields.Selection(selection=[('good', 'Good'),('normal', 'Normal'), ('bad', 'Bad')],string="Trust")


    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.trust = self.partner_id.trust



class TrustContact(models.Model):
    _inherit = 'res.partner'
    trust = fields.Selection(string="Trust",
                             selection=[('good', 'Good'),
                                        ('normal', 'Normal'),
                                        ('bad', 'Bad')])

class TrustInvoice(models.Model):
    _inherit = 'account.move'
    trust = fields.Selection(string="Trust",
                             selection=[('good', 'Good'),
                                        ('normal', 'Normal'),
                                        ('bad', 'Bad')])
