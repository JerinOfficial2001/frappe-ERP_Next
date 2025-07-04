import frappe
from frappe.utils import now

@frappe.whitelist()
def add_part_to_cart(part_name):
    user = frappe.session.user
    doc = frappe.get_doc({
        'doctype': 'User Cart',
        'user': user,
        'mobile_part': part_name,
        'order_date': now(),
        'status': 'Received'
    })
    doc.insert()
    return "Part added to your cart"
