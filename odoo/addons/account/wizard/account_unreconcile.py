# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, api


class AccountUnreconcile(models.TransientModel):
    _name = "account.unreconcile"
    _description = "Account Unreconcile"

    @api.multi
    def trans_unrec(self):
        context = dict(self._context or {})
        if context.get('active_ids', False):
            self.env['account.move.line'].browse(context.get('active_ids')).remove_move_reconcile()
        return {'type': 'ir.actions.act_window_close'}