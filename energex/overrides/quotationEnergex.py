import frappe
from erpnext.selling.doctype.quotation.quotation import Quotation

class QuotationEnergex(Quotation):

    def update_opportunity_status(self, status, opportunity=None):
        
        if not opportunity:
            opportunity = self.opportunity

        opp = frappe.get_doc("Opportunity", opportunity)

        if self.method == "on_submit":
            if self.currency == 'USD':
                opp.opportunity_amount = self.base_total
            else:
                opp.opportunity_amount = self.total
            opp.save()
            
        opp.set_status(status=status, update=True)
       
    