import frappe
from frappe.utils import cint

def qp_boot_session(bootinfo):
    """Get Settings"""
    print("------------qp_boot_session------------------")

    if frappe.session['user']!='Guest':

        bootinfo.selling_default_valid_till = cint(frappe.db.get_single_value('Selling Settings', 'default_valid_till'))
