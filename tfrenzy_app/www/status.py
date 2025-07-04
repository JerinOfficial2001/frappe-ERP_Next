import frappe

def get_context(context):
    name = frappe.form_dict.get("name")
    doc = frappe.get_doc("TFrenzy DocType", name)
    context.product = doc
    context.status = doc.refurbishment_status
    context.steps = ["Received", "Diagnosed", "In Repair", "QC Passed", "Ready for Sale"]
