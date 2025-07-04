import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def add_product(spare_name, image):
    if not spare_name:
        return {"error": "Missing spare_name"}

    doc = frappe.get_doc({
        "doctype": "TFrenzy DocType",
        "spare_name": spare_name,
        "image": image
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
    return {"success": True, "name": doc.name}
